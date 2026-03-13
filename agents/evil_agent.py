from engine.answer_engine import generate_response

PROMPT = """
You are a mischievous villain with dark humor.

Answer sarcastically but humorously.

Rules:
- one sentence
"""


def evil_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)