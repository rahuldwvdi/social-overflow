from engine.answer_engine import generate_response

PROMPT = """
You are an AI researcher.

Give one scientific statement.

Rules:
- one sentence
- max 15 words
- add one emoji

Answer:
"""


def research_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)