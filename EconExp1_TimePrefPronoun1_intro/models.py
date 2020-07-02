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

from EconExp1_TimePrefPronoun1_questionaire.models import (
    OptionOfGetMoney,
    WaitingPeriod,
    GainedAmount,
    Treatment,
    Subsession as QuestionaireSubsession
)


author = 'Josie_NTULAB'

doc = """
決策實驗-說明部分
"""


class Constants(BaseConstants):
    name_in_url = 'EconExp1_intro'
    players_per_group = None
    num_rounds = 1

    gained_amount_today = GainedAmount.today


class Subsession(BaseSubsession):
    num_questions = models.IntegerField() # 實際上的回合數

    def creating_session(self):
        # 確保 `WaitingPeriod/GainedAmount` 有從 session config 載入好。
        QuestionaireSubsession.load_from_session_config_if_needed(self.session.config)
        
        self.num_questions = len(WaitingPeriod.list) * len(GainedAmount.list)
        
        Treatment.create_pronoun_list_if_needed(self.get_players())
        Treatment.create_speech_speed_list_if_needed(self.get_players())
        for p in self.get_players():
            p.treatment_pronoun = Treatment.get_pronoun(p)
            p.treatment_speech_speed = Treatment.get_speech_speed(p)


class Group(BaseGroup):
    pass


class Player(BasePlayer): # TODO：有空再尋找能直接繼承（重複利用）EconExp1_TimePrefPronoun1_questionaire.models 裡 Player 的方法
    # 幾週後 (hidden)
    waiting_period = models.IntegerField()

    # 獲得的報償 (hidden)
    gained_amount = models.IntegerField()

    # treatement 主詞（hidden）
    treatment_pronoun = models.StringField(initial = '')

    # treatement 語音速度（hidden）
    treatment_speech_speed = models.FloatField(initial = 0)

    get_money_now_or_future = models.StringField(
        blank=True, # optional，可不作答的意思。「範例時其實不需要他們做選擇」
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


