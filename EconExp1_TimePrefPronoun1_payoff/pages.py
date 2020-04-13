from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants

from EconExp1_TimePrefPronoun1_questionaire.models import (
    Constants as QuestionaireConstants,
    GainedAmount,
)

class PayoffInformation(Page):
    form_model = 'player'
    form_fields = [
		'waiting_period',
	   	'gained_amount',
	    'bank_code',
	   	'account_number',
	   	]
	   	
    def vars_for_template(self):
        return self.participant.vars['selected_questionaire']

    def is_displayed(self):
    	# 在畫面顯示前自動代入之前抽出的結果，存進 db。
        self.fill_out_selection_result_fields(self.player)
        return True

    def fill_out_selection_result_fields(self, player):
        selected_q = self.participant.vars['selected_questionaire']
        if selected_q['selected_get_money_now']:
            player.waiting_period = 0
            player.gained_amount = GainedAmount.get_TWD_today()
        else:
            player.waiting_period = selected_q['selected_waiting_period'] 
            player.gained_amount = selected_q['selected_gained_amount'] 


page_sequence = [PayoffInformation]
