import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.1-8b-instant"

def generate_response(prompt: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=30,
        temperature=0.3
    )

    text = response.choices[0].message.content
    return text.split("\n")[0].strip()