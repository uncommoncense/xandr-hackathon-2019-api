import json
from fastapi import FastAPI
from chatbot import MastodonBot
from dotenv import load_dotenv
from model.predict import PredictionModel
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

origins = [
    "https://47edbf88.ngrok.io",
    "http://47edbf88.ngrok.io",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = MastodonBot()
predictionModel = PredictionModel()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/analyze/{test}")
def analyze(test: str):
    prediction = predictionModel.predict(test)
    return {"input": test,
            "prediction": prediction,
            "filter": True if prediction > 0.5 else False}


@app.get("/report/{user}/{status_id}")
def report(user: str, status_id: int):
    return bot.reply_to(user, status_id)

