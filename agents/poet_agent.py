from engine.answer_engine import generate_response

PROMPT = """
You are a poetic thinker.

Answer the question like a short poetic thought.

Rules:
- one sentence
- expressive
- max 20 words
"""


def poet_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)