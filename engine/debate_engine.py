from agents.poet_agent import poet_agent
from agents.artist_agent import artist_agent
from agents.techy_agent import techy_agent
from agents.god_agent import god_agent
from agents.drunk_agent import drunk_agent
from agents.philosopher_agent import philosopher_agent
from agents.evil_agent import evil_agent


def run_debate(question: str):

    responses = {}

    responses["Poet"] = poet_agent(question)
    responses["Artist"] = artist_agent(question)
    responses["Techy"] = techy_agent(question)
    responses["God"] = god_agent(question)
    responses["Drunk Man"] = drunk_agent(question)
    responses["Philosopher"] = philosopher_agent(question)
    responses["Evil but Funny"] = evil_agent(question)

    return {
        "arguments": responses
    }