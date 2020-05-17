from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, WaitingPeriod, GainedAmount
from random import randint
import random
from EconExp1_TimePrefPronoun1_questionaire.models import Subsession as QuestionaireSubsession


class GetMoneyNowOrFuture(Page):
    form_model = 'player'
    form_fields = [
    	'waiting_period',
    	'gained_amount',
        'treatment_pronoun',
    	'get_money_now_or_future', 
    	'num_listen_times', 'decision_duration',
    	]

    def generate_questionaire_parameters_pairs(self):
        q_params_pairs = []
        # 產生所有週數和金額的組合
        shuffled_waiting_period = WaitingPeriod.list
        random.shuffle(shuffled_waiting_period) # 打亂順序
        for each_waiting_period in shuffled_waiting_period:
          for each_gained_amount in GainedAmount.list:
            q_params_pairs.append(
              dict(
                waiting_period = each_waiting_period,
                gained_amount = each_gained_amount,
              )
            )
        return q_params_pairs

    def setup_questionaire_parameters_pairs(self):
        # 確保 `WaitingPeriod/GainedAmount` 有從 session config 載入好。
        QuestionaireSubsession.load_from_session_config_if_needed(self.session.config)

        # 如果還不存在，就現在產生「週數和金額的組合」並存起來
        # 如果已經存在，就取出
        if Constants.key_q_params_pairs not in self.participant.vars: 
            pairs = self.generate_questionaire_parameters_pairs()
            self.participant.vars[Constants.key_q_params_pairs] = pairs
        q_params_pairs = self.participant.vars[Constants.key_q_params_pairs]

        # 設定每一 round 的參數，並寫入 db
        idx = self.round_number - 1 # list 從0開始 但 round_number 從1開始
        pair = q_params_pairs[idx]
        self.player.waiting_period = pair['waiting_period']
        self.player.gained_amount = pair['gained_amount']

    def select_questionaire(self):
        q_params_pairs = self.participant.vars[Constants.key_q_params_pairs]
        selected_idx = randint(1, Constants.actual_num_rounds()) - 1 # list 的 index 從0開始 但 round_number 從1開始
        selected_q_parama_pair = q_params_pairs[selected_idx]
        selected_player = self.player.in_all_rounds()[selected_idx]
        selected_player.is_selected = True
        self.participant.vars[Constants.key_selected_q] = dict(
            selected_round_number = selected_idx + 1,
            selected_waiting_period = selected_q_parama_pair['waiting_period'],
            selected_gained_amount = selected_q_parama_pair['gained_amount'],
            selected_get_money_now = selected_player.get_money_now_or_future == 'now',
            )

    def is_displayed(self):
        # 設定每一 round 的參數（如週數和金額）
        self.setup_questionaire_parameters_pairs()
        return True

    def before_next_page(self):
        if self.round_number == Constants.actual_num_rounds():
            # 只在最後一回合才抽結果
            self.select_questionaire()

    def app_after_this_page(self, upcoming_apps): # https://otree.readthedocs.io/en/latest/pages.html#app-after-this-page
        # 把週數和金額的組合都跑完後，當下這個 app 就可以結束了
        if self.round_number >= Constants.actual_num_rounds():
            return upcoming_apps[0]
        else:
            pass


page_sequence = [GetMoneyNowOrFuture]
