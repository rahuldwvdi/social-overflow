from engine.answer_engine import generate_response

PROMPT = """
You are a philosopher.

Give a thoughtful insight.

Rules:
- one sentence
- max 15 words
- add one emoji

Answer:
"""


def philosophy_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)