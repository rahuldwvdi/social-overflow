from engine.answer_engine import generate_response

PROMPT = """
You are a startup founder.

Give a bold opinion.

Rules:
- one sentence
- max 15 words
- add one emoji

Answer:
"""


def startup_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)