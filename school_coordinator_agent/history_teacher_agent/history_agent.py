from google.adk.agents.llm_agent import Agent

history_teacher_agent = Agent(
    model='gemini-2.0-flash',
    name='history_teacher_agent',
    description='A specialized agent that helps with history.',
    instruction='You are an expert history teacher. Help the user with historical events, civilizations, timelines, and historical analysis.',
)
