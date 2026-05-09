from google.adk.agents.llm_agent import Agent

science_teacher_agent = Agent(
    model='gemini-2.0-flash',
    name='science_teacher_agent',
    description='A specialized agent that helps with science subjects.',
    instruction='You are an expert science teacher. Help the user with physics, chemistry, biology, and general science concepts.',
)
