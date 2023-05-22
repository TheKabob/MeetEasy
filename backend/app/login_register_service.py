import logging

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from app.Model.Model import register_user, login_user
from app.dao.login_register_dao import register, login

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:8000",
    # Add any additional origins that should be allowed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logger = logging.getLogger("my-logger")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


@app.post("/register")
def register_user(body: register_user):
    try:
        logger.info(f"Registering {body.name}")
        return register(body.name, body.email, body.password)
    except Exception as e:
        logger.error(str(e))


@app.post("/login")
def login_user(body: login_user):
    try:
        logger.info(f"Logging in {body.email}")
        return login(body.email, body.password)
    except Exception as e:
        logger.error(str(e))


@app.get("/app_status")
async def app_status():
    try:
        return {"status": "ok"}
    except Exception as e:
        logger.error(str(e))


if __name__ == '__main__':
    uvicorn.run(app=app, port=9090)
