import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "tinyllama"


def generate_response(prompt: str):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 120
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)

    data = response.json()

    return data["response"]