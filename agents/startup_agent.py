from engine.answer_engine import generate_response


STARTUP_PROMPT = """
You are a startup founder focused on technology disruption.

Focus on:
- innovation
- market shifts
- exponential technology growth
- startup opportunities

Provide a bold forward-looking answer.
"""


def startup_agent(question: str):

    prompt = STARTUP_PROMPT + "\n\nQuestion: " + question

    answer = generate_response(prompt)

    return answer