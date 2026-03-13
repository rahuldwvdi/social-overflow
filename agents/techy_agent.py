from engine.answer_engine import generate_response

PROMPT = """
You are a tech enthusiast.

Explain things in a logical tech-style analogy.

Rules:
- one short sentence
"""


def techy_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)