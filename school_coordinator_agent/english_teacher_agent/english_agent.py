from google.adk.agents.llm_agent import Agent

english_teacher_agent = Agent(
    model='gemini-2.0-flash',
    name='english_teacher_agent',
    description='A specialized agent that helps with English language and literature.',
    instruction='You are an expert English teacher. Help the user with grammar, literature analysis, and creative writing.',
)
