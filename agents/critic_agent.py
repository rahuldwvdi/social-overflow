from engine.answer_engine import generate_response


PROMPT = """
You are a debate judge.

Evaluate arguments based on logic and clarity.

Output format:

Best Agent:
Confidence:
Reason:
"""


def critic_agent(question: str, arguments: dict):

    text = ""

    for agent, answer in arguments.items():
        text += f"{agent}: {answer}\n"

    prompt = PROMPT + "\nQuestion: " + question + "\nArguments:\n" + text

    return generate_response(prompt)