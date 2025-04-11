from decouple import config


def get_tushare_key() -> str:
    SECRET_KEY = config('TuShareKey')
    return SECRET_KEY
