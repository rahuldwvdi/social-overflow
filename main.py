from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from engine.debate_engine import run_debate

app = FastAPI()


@app.get("/debate")
def debate(question: str):

    result = run_debate(question)

    return result


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")