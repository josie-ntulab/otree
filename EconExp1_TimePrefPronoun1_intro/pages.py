from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from EconExp1_TimePrefPronoun1_questionaire.pages import GetMoneyNowOrFuture


class Intro_1(Page):
    form_model = 'player'


class Intro_2(Page):
    form_model = 'player'


class Intro_3(GetMoneyNowOrFuture):
    def is_displayed(self):
    	# 「範例」中固定參數為 2 和 120（如果您選擇未來的報酬，那代表您會在2週後得到120元。）
        self.player.waiting_period = 2
        self.player.gained_amount = 120
        return True

    def before_next_page(self):
    	# override 掉繼承的 `GetMoneyNowOrFuture` class 中的行為，此處不做事。
        pass

    def app_after_this_page(self, upcoming_apps):
    	# override 掉繼承的 `GetMoneyNowOrFuture` class 中的行為，此處不做事。
    	pass


class Intro_4(Page):
    form_model = 'player'
    
    
class Intro_5(Page):
    form_model = 'player'


page_sequence = [Intro_1, Intro_2, Intro_3, Intro_4, Intro_5]
