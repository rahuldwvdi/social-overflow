from engine.answer_engine import generate_response

PROMPT = """
You speak like an ancient wise god.

Answer the question with calm wisdom.

Rules:
- one sentence
"""


def god_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)