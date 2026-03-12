from engine.answer_engine import generate_response


CRITIC_PROMPT = """
You are an expert debate judge evaluating arguments between AI agents.

Evaluation criteria:
- logical reasoning
- technical accuracy
- practical relevance
- clarity of argument

Rules:
- Select the best argument
- Provide a confidence score from 0 to 1
- Explain your reasoning briefly
"""


def critic_agent(question: str, arguments: dict):

    debate_text = ""

    for agent, answer in arguments.items():
        debate_text += f"{agent}: {answer}\n"

    prompt = f"""
{CRITIC_PROMPT}

Question:
{question}

Arguments:
{debate_text}

Provide output in this format:

Best Agent:
Confidence:
Reason:
"""

    evaluation = generate_response(prompt)

    return evaluation