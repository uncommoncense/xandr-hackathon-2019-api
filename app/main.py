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
def analyze_text(test: str):
    return {"input": {test},
            "filter": True if random() > 0.5 else False}


@app.get("/alert/{user}")
def alert(user: str, status: str):
    return {"user:": {user},
            "status": {status}}


@app.get("/test")
def test():
    bot.reply_to(103318476731759999)
