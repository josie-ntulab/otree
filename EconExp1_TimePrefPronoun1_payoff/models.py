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
    Constants as QuestionaireConstants,
    GainedAmount,
)


author = 'Josie_NTULAB'

doc = """
決策實驗-匯款資訊部分
"""


class Constants(BaseConstants):
    name_in_url = 'EconExp1_payoff'
    players_per_group = None
    num_rounds = 1
    gained_amount_today = GainedAmount.today


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 幾週後
    waiting_period = models.IntegerField()

    # 獲得的報償
    gained_amount = models.IntegerField()

    # 匯款 銀行代碼
    bank_code = models.StringField()

    # 匯款 銀行帳號
    account_number = models.StringField(
        label = '請輸入你的銀行帳號', 
        )