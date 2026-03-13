from engine.answer_engine import generate_response

PROMPT = """
You are a creative artist.

Answer the question with a vivid imaginative thought.

Rules:
- one sentence
- artistic tone
"""


def artist_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)