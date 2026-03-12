from engine.answer_engine import generate_response


PHILOSOPHY_PROMPT = """
You are a philosopher studying technology and society.

Focus on:
- ethics
- long-term human impact
- societal consequences
- philosophical implications

Provide a thoughtful reflective answer.
"""


def philosophy_agent(question: str):

    prompt = PHILOSOPHY_PROMPT + "\n\nQuestion: " + question

    answer = generate_response(prompt)

    return answer