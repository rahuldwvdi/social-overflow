import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "tinyllama"


def generate_response(prompt: str):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 30,      # limit output length
            "temperature": 0.2,     # reduce randomness
            "top_p": 0.9
        }
    }

    try:

        response = requests.post(OLLAMA_URL, json=payload)

        data = response.json()

        text = data["response"]

        # ---- CLEAN OUTPUT ----

        text = text.strip()

        # remove common junk phrases
        junk = [
            "Sure!",
            "Sure.",
            "Sure thing",
            "Here is",
            "Here's",
            "Answer:",
            "Response:",
            "The answer is"
        ]

        for j in junk:
            text = text.replace(j, "")

        # keep only first line
        text = text.split("\n")[0]

        # enforce max length
        if len(text) > 120:
            text = text[:120]

        return text.strip()

    except Exception as e:

        return "model_error ⚠️"