import os

class Config(object):
    # The bot-token which you can get from @Botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1426271190:AAGRFRQ9wa0WTpPz58t_6UwYf1A0ByyhWok")
    # There is no measure to limit who can use this bot, so add userids of users authorized to use this bot
    AUTH_USERS = os.environ.get("AUTH_USERS", "1562091466")
    # Add numbers below who shouldn't be bombed ever
    NO_BOMB_NUMS = os.environ.get("NO_BOMB_NUMS", "semx")
    # Add userids below of users who should have sudo authority over bot, i.e., have no bombing limits
    GOD_USERS = os.environ.get("GOD_USERS", "1047091391 1895963967")
