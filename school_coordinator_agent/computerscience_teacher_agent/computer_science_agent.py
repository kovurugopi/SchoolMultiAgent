from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

computerscience_teacher_agent = Agent(
    model='gemini-2.0-flash',
    name='computerscience_teacher_agent',
    description='A specialized agent that helps with computer science subjects.',
    instruction='You are an expert computer science teacher. Help the user with programming, algorithms, data structures, databases, networking, and all computer science concepts. Use the google_search tool to look up current documentation, tutorials, or technical information when needed.',
    tools=[google_search],
)
