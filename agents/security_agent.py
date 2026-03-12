from engine.answer_engine import generate_response


SECURITY_PROMPT = """
You are a cybersecurity expert.

Focus on:
- vulnerabilities
- system risks
- misuse of AI technology
- safety concerns

Provide a cautious and risk-aware answer.
"""


def security_agent(question: str):

    prompt = SECURITY_PROMPT + "\n\nQuestion: " + question

    answer = generate_response(prompt)

    return answer
