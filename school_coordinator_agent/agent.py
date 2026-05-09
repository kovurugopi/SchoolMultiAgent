from google.adk.agents.llm_agent import Agent
from .english_teacher_agent.english_agent import english_teacher_agent
from .maths_teacher_agent.maths_agent import maths_teacher_agent
from .science_teacher_agent.science_agent import science_teacher_agent
from .history_teacher_agent.history_agent import history_teacher_agent
from .geography_teacher_agent.geography_agent import geography_teacher_agent
from .computerscience_teacher_agent.computer_science_agent import computerscience_teacher_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
   description="Main router agent that sends tasks to sub-agents.",
    instruction="""
You are the school coordinator.
 
Route user requests:
 
- If user asks about English, grammar, literature, or creative writing → use english_teacher_agent
- If user asks about maths, calculations, algebra, or geometry → use maths_teacher_agent
- If user asks about science, physics, chemistry, or biology → use science_teacher_agent
- If user asks about history, historical events, or civilizations → use history_teacher_agent
- If user asks about geography, countries, maps, continents, or physical features → use geography_teacher_agent
- If user asks about computer science, programming, algorithms, data structures, or networking → use computerscience_teacher_agent

If unsure, respond directly.
""",
    sub_agents=[english_teacher_agent, maths_teacher_agent, science_teacher_agent, history_teacher_agent, geography_teacher_agent, computerscience_teacher_agent]
)
