from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/analyze/{test}")
def analyze_text(test: str):
    return {"input": {test},
            "toxicity": 2.0}


@app.get("/alert/{user}?status={status}")
def alert(user: str, status: str):
    return {"user:": {user},
            "status": {status}}
