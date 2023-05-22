import logging
import time

import psycopg2
from fastapi import HTTPException

from app.utils import get_traceback
from app.settings import db_config, cfg

logger = logging.getLogger("my-logger")


def db_connect(connection_details):
    retry_count = 0
    while retry_count < int(cfg.db_max_retry_count):
        try:
            return psycopg2.connect(**connection_details)
        except psycopg2.Error as e:
            retry_count += 1
            logger.error(
                "Error occurred: %s, retrying (%d/%d)",
                str(e),
                retry_count,
                cfg.db_max_retry_count,
            )
            if retry_count == cfg.db_max_retry_count:
                logger.info("failed to connect to database")
                raise HTTPException(
                    status_code=400,
                    detail=f"DB exception: Unable to connect to DB {str(e)}",
                )
            time.sleep(0.01)
        except Exception as e:
            logger.error(f"Unknown Exception Occurred: {get_traceback(e)}")
            raise HTTPException(
                status_code=500, detail=f"Internal Server Error: {str(e)}"
            )


conn = db_connect(db_config.conn_info)
