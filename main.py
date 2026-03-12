from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import sqlite3

from engine.debate_engine import run_debate
from memory.database import create_tables

app = FastAPI()

# create database tables
create_tables()


@app.get("/")
def home():
    return {"message": "Social Overflow API is running"}


@app.get("/debate")
def debate(question: str):

    result = run_debate(question)

    return {
        "question": question,
        "debate": result
    }


@app.get("/debates")
def get_debates():

    conn = sqlite3.connect("debates.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM debates")

    rows = cursor.fetchall()

    conn.close()

    return rows


# serve frontend
app.mount("/app", StaticFiles(directory="frontend", html=True), name="frontend")