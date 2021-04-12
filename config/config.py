import yaml
from pymongo import MongoClient

# Настройка конфигураций для подключения и работы с MongoDB


def load_config() -> dict:
    with open('config/config.yml') as yaml_file:
        conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    return conf


CONF = load_config()

DB_CLIENT = MongoClient(
    host=CONF.get("databases", dict())["default"]["HOST"],
    port=CONF.get("databases", dict())["default"]["PORT"],
)

DB = DB_CLIENT[CONF.get("databases", dict())["default"]["NAME"]]


def close_db_client():
    DB_CLIENT.close()
