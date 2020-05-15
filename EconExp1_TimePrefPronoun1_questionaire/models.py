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
    available_pronoun_list = ['你', '受試者']
    def get_pronoun(player):
        participant = player.participant
        # lazy loading: 若不存在就決定並起來，若已存在就直接取出
        if Constants.key_pronoun not in participant.vars:
            # 從上面定義的 treatment 列表中，隨機選出一個給該受試者
            participant.vars[Constants.key_pronoun] = random.choice(Treatment.available_pronoun_list)
        pronoun = participant.vars[Constants.key_pronoun]
        return pronoun


class Constants(BaseConstants):
    name_in_url = 'EconExp1_questionaire'
    players_per_group = None
    num_rounds = 24 # 這裡代表最大可能 rounds 數，實際的 rounds 數請參考 actual_num_rounds()
    key_q_params_pairs = 'questionaire_parameters_pairs'
    key_selected_q = 'selected_questionaire'
    key_pronoun = 'treatment_pronoun'

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
        for p in self.get_players():
            p.treatment_pronoun = Treatment.get_pronoun(p)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 幾週後 (hidden)
    waiting_period = models.IntegerField()

    # 獲得的報償 (hidden)
    gained_amount = models.IntegerField()

    treatment_pronoun = models.StringField(initial = '')

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
    
