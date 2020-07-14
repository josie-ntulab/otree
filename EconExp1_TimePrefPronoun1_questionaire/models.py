from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from enum import Enum
import random
import json

author = 'Josie_NTULAB'

doc = """
決策實驗-問卷部分
"""


class WaitingPeriod(object):
    list = []

class GainedAmount(object):
    list = []
    today = 100

class Treatment(object):    
    participant_ids = []
    
    def create_participant_ids(all_players):
        for p in all_players:
            pid = p.participant.id_in_session
            if pid not in Treatment.participant_ids:
                Treatment.participant_ids.append(pid)

    available_pronoun_list = ['我']
    pronoun_list = []
    
    def create_pronoun_list_if_needed(all_players): # 事先準備好所有受試者的 pronoun 們
        if len(Treatment.pronoun_list) > 0:
            return
        Treatment.create_participant_ids(all_players)
        for each_pronoun in Treatment.available_pronoun_list:
            count = int(len(Treatment.participant_ids) / len(Treatment.available_pronoun_list)) # 例如有5人，平均分配兩組 treatment，那就是 5/2 = 2（不取餘數）
            Treatment.pronoun_list.extend( [each_pronoun] * count ) # “python - Create list of single item repeated N times - Stack Overflow” https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times
        while len(Treatment.pronoun_list) < len(Treatment.participant_ids): # 若因前面 for 迴圈中不能整除，也就是 `available_pronoun_list` 不能完平均地分配給所有 participants，則最後會不夠，在此補上。（如果 `available_pronoun_list` 就兩個，那最多就差1，也就是最多會差到(count - 1)個）
            Treatment.pronoun_list.append(random.choice(Treatment.available_pronoun_list)) # 剩下的就隨機挑選
        random.shuffle(Treatment.pronoun_list) # 把例如 [你, 你, 你, 受試者, 受試者] 打亂成 [受試者, 你, 你, 受試者, 你]

    def get_pronoun(player):
        participant = player.participant
        # lazy loading: 若不存在就取得並存起來，若已存在就直接取出
        if Constants.key_pronoun not in participant.vars:
            # 從上面定義的 treatment pronoun_list 列表中，取出該受試者的 pronoun
            pid = participant.id_in_session
            idx_of_participants = Treatment.participant_ids.index(pid)
            participant.vars[Constants.key_pronoun] = Treatment.pronoun_list[idx_of_participants]
        pronoun = participant.vars[Constants.key_pronoun]
        return pronoun

    available_speech_speed_list = [0.7, 0.8, 0.9]
    speech_speed_list = []

    def create_speech_speed_list_if_needed(all_players): # 事先準備好所有受試者的 speech_speed 們
        if len(Treatment.speech_speed_list) > 0:
            return
        Treatment.create_participant_ids(all_players)
        for each_speed in Treatment.available_speech_speed_list:
            count = int(len(Treatment.participant_ids) / len(Treatment.available_speech_speed_list)) # 例如有5人，平均分配兩組 treatment，那就是 5/2 = 2（不取餘數）
            Treatment.speech_speed_list.extend( [each_speed] * count ) # “python - Create list of single item repeated N times - Stack Overflow” https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times
        while len(Treatment.speech_speed_list) < len(Treatment.participant_ids): # 若因前面 for 迴圈中不能整除，也就是 `speech_speed_list` 不能完平均地分配給所有 participants，則最後會不夠，在此補上。（如果 `speed_available_list` 就兩個，那最多就差1，也就是最多會差到(count - 1)個）
            Treatment.speech_speed_list.append(random.choice(Treatment.available_speech_speed_list)) # 剩下的就隨機挑選
        random.shuffle(Treatment.speech_speed_list) # 打亂原有 list 順序
    
    def get_speech_speed(player):
        participant = player.participant
        # lazy loading: 若不存在就取得並存起來，若已存在就直接取出
        if Constants.key_speech_speed not in participant.vars:
            # 從上面定義的 treatment speech_speed_list 列表中，取出該受試者的 speech_speed
            pid = participant.id_in_session
            idx_of_participants = Treatment.participant_ids.index(pid)
            participant.vars[Constants.key_speech_speed] = Treatment.speech_speed_list[idx_of_participants]
        speech_speed_list = participant.vars[Constants.key_speech_speed]
        return speech_speed_list


class Constants(BaseConstants):
    name_in_url = 'EconExp1_questionaire'
    players_per_group = None
    num_rounds = 24 # 這裡代表最大可能 rounds 數，實際的 rounds 數請參考 actual_num_rounds()
    key_q_params_pairs = 'questionaire_parameters_pairs'
    key_selected_q = 'selected_questionaire'
    key_pronoun = 'treatment_pronoun'
    key_speech_speed = 'treatment_speech_speed'

    def actual_num_rounds():
        return min(Constants.num_rounds, len(WaitingPeriod.list) * len(GainedAmount.list)) # 取其中最小的


class OptionOfGetMoney(Enum):
    OPTION_NOW = '選擇今天的報酬'
    OPTION_FUTURE = '選擇未來的報酬'

    def formatted_option(player, option_enum):
        return Treatment.get_pronoun(player) + option_enum.value
        

class Subsession(BaseSubsession):
    @staticmethod
    def load_from_session_config_if_needed(session_config):
        # 從 session config 讀取（預設定義在 settings.py 中 SESSION_CONFIGS，但可在網頁的「Create a new session / Configure session」 中修改）
        if len(WaitingPeriod.list) == 0:
            json_string = session_config['available_waiting_periods']
            WaitingPeriod.list = json.loads(json_string)

        if len(GainedAmount.list) == 0:
            json_string = session_config['available_gained_amounts']
            GainedAmount.list = json.loads(json_string)

    def creating_session(self):
        Subsession.load_from_session_config_if_needed(self.session.config)
        Treatment.create_pronoun_list_if_needed(self.get_players())
        Treatment.create_speech_speed_list_if_needed(self.get_players())
        for p in self.get_players():
            p.treatment_pronoun = Treatment.get_pronoun(p)
            p.treatment_speech_speed = Treatment.get_speech_speed(p)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 幾週後 (hidden)
    waiting_period = models.IntegerField()

    # 獲得的報償 (hidden)
    gained_amount = models.IntegerField()

    # treatement 主詞（hidden）
    treatment_pronoun = models.StringField(initial = '')

    # treatement 語音速度（hidden）
    treatment_speech_speed = models.FloatField(initial = 0)

    get_money_now_or_future = models.StringField(
        label = '請選擇您要今天或未來的報酬', 
        widget = widgets.RadioSelect, 
        )
    def get_money_now_or_future_choices(self):
        return [
            ['now', OptionOfGetMoney.formatted_option(self, OptionOfGetMoney.OPTION_NOW)],
            ['future', OptionOfGetMoney.formatted_option(self, OptionOfGetMoney.OPTION_FUTURE)],
            ]

    # 聽了幾次，單位為次數 (hidden，根據使用者行為紀錄)
    num_listen_times = models.IntegerField(initial = 0)

    # 決策時長，單位為秒數 (hidden，根據使用者行為紀錄)
    decision_duration = models.FloatField(initial = 0)

    # 是否為最後電腦選中的 round (hidden，最後一回合會抽出並寫入)
    is_selected = models.BooleanField(initial = False)
    
