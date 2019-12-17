import json
from fastapi import FastAPI
from chatbot import MastodonBot
from dotenv import load_dotenv
from random import random

load_dotenv()

app = FastAPI()
bot = MastodonBot()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/analyze/{test}")
def analyze(test: str):
    return {"input": test,
            "filter": True if random() > 0.5 else False}


@app.get("/report/{user}/{status_id}")
def report(user: str, status_id: int):
    return bot.reply_to(user, status_id)

