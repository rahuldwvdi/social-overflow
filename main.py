from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from engine.debate_engine import run_debate
import os

app = FastAPI()


@app.get("/debate")
def debate(question: str):

    result = run_debate(question)

    return result


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )