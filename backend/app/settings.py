import os


class Configuration:
    db_max_retry_count = os.environ["DB_MAX_RETRY_COUNT"]


class DBConfig:
    conn_info = {
        "host": os.environ["HOST"],
        "port": os.environ["PORT"],
        "database": os.environ["DATABASE"],
        "user": os.environ["USER"],
        "password": os.environ["PASSWORD"],
    }


db_config = DBConfig()
cfg = Configuration()
