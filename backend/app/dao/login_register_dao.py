import logging

from fastapi import HTTPException
from starlette import status

from app.dao import conn
from app.settings import cfg

logger = logging.getLogger("my-logger")
logger.setLevel("INFO")


def register(name, email, password):
    retry_count = 0
    while retry_count < int(cfg.db_max_retry_count):
        try:
            cur = conn.cursor()

            # Check if user with the same email already exists
            check_query = "SELECT COUNT(*) FROM users WHERE email = %s"
            cur.execute(check_query, (email,))
            count = cur.fetchone()[0]

            if count > 0:
                # User with the same email already exists
                cur.close()
                conn.rollback()  # Rollback any changes made
                return {"message": "User already exists. Please login instead."}

            # Insert the new user
            insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            user_data = (name, email, password)
            cur.execute(insert_query, user_data)
            cur.close()
            conn.commit()
            return {"message": "User registered successfully"}

        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


def login(email, password):
    retry_count = 0
    while retry_count < int(cfg.db_max_retry_count):
        try:
            cur = conn.cursor()

            # Check if user with the email and password exists
            login_query = "SELECT COUNT(*) FROM users WHERE email = %s AND password = %s"
            cur.execute(login_query, (email, password))
            count = cur.fetchone()[0]

            if count == 1:
                # User with the email and password exists
                cur.close()
                logger.info(f"logged in {email}")
                return {"message": "Logged in successfully"}
            else:
                cur.close()
                logger.info(f"user with {email} does not exists")
                return {"message": "User not found. Please register."}

        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
