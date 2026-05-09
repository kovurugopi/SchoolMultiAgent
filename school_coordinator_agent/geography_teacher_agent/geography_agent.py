from google.adk.agents.llm_agent import Agent

geography_teacher_agent = Agent(
    model='gemini-2.0-flash',
    name='geography_teacher_agent',
    description='A specialized agent that helps with geography subjects.',
    instruction='You are an expert geography teacher. Help the user with countries, capitals, continents, maps, physical features, climate, and all geography concepts.',
)
