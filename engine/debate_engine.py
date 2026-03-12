from agents.engineer_agent import engineer_agent
from agents.research_agent import research_agent
from agents.startup_agent import startup_agent
from agents.security_agent import security_agent
from agents.philosophy_agent import philosophy_agent
from memory.retrieval import find_similar_question
from agents.critic_agent import critic_agent
from engine.critique_engine import generate_critique

from memory.database import save_debate


def run_debate(question: str):
    previous = find_similar_question(question)

    if previous:

        return {
            "message": "Previous debate found",
            "question": previous[0],
            "best_agent": previous[1],
            "confidence": previous[2],
            "evaluation": previous[3]
        }
    # Round 1 — Initial Arguments
    responses = {}

    responses["Engineer Agent"] = engineer_agent(question)
    responses["Research Agent"] = research_agent(question)
    responses["Startup Agent"] = startup_agent(question)
    responses["Security Agent"] = security_agent(question)
    responses["Philosophy Agent"] = philosophy_agent(question)

    # Round 2 — Critiques
    critiques = {}

    for agent in responses:

        other_arguments = ""

        for other_agent, answer in responses.items():

            if other_agent != agent:
                other_arguments += f"{other_agent}: {answer}\n"

        critiques[agent] = generate_critique(agent, question, other_arguments)

    # Round 3 — Critic Evaluation
    evaluation = critic_agent(question, responses)

    best_agent = "Unknown"
    confidence = 0.0

    lines = evaluation.split("\n")

    for line in lines:

        if "Best Agent" in line:
            best_agent = line.split(":")[-1].strip()

        if "Confidence" in line:
            try:
                confidence = float(line.split(":")[-1].strip())
            except:
                confidence = 0.0

    # Save debate in database
    save_debate(question, best_agent, confidence, evaluation)

    return {
        "arguments": responses,
        "critiques": critiques,
        "evaluation": evaluation
    }