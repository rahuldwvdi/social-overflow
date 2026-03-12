from engine.answer_engine import generate_response

PROMPT = """
You are a software engineer.

Respond in ONE short sentence only.

Rules:
- no explanations
- no introductions
- no extra text
- no repeating the question
- max 15 words
- add one emoji

Answer:
"""


def engineer_agent(question: str):

    prompt = f"{PROMPT} {question}"

    return generate_response(prompt)