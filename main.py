from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from engine.debate_engine import run_debate
from memory.database import create_tables

app = FastAPI()

create_tables()


@app.get("/debate")
def debate(question: str):

    result = run_debate(question)

    return {
        "question": question,
        "debate": result
    }


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")