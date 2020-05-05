from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    # dict(
    #    name='public_goods',
    #    display_name="Public Goods",
    #    num_demo_participants=3,
    #    app_sequence=['public_goods', 'payment_info']
    # ),
    # dict(
    #     name='authentication_survey',
    #     display_name="Authentication Survey",
    #     num_demo_participants=1,
    #     app_sequence=['authentication_survey']
    # ),
    dict(
        name='EconExp1_TimePrefPronoun1',
        display_name="EconExp1",
        num_demo_participants=3,
        app_sequence=[
            'EconExp1.intro',
            'EconExp1.q', 
            'EconExp1.survey', 
            'EconExp1.selection_result',
            'EconExp1.payoff',
            'EconExp1.finished',
            ],

        # Configure sessions https://otree.readthedocs.io/en/latest/treatments.html#configure-sessions
        available_waiting_periods='[1, 4, 12]',
        available_gained_amounts='[105, 110, 115, 120, 125, 130, 135, 140]',
        doc="""
            請在「Configure session 的 Custom 中」定義所有「等待週數」和「獲得金額」的列表
            """
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab',
        participant_label_file='_rooms/econ.txt',
        #use_secure_urls=True
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'ao8%9gfcywbe)d(rw_^+31chpf7jbv4=n068&37nwi8qo5=n8c'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
