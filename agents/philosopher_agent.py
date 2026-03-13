from engine.answer_engine import generate_response

PROMPT = """
You are a philosopher reflecting on life.

Answer with a deep but simple insight.

Rules:
- one thoughtful sentence
"""


def philosopher_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)