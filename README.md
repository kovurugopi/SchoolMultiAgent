# School Multi-Agent System

A multi-agent system built with [Google ADK (Agent Development Kit)](https://google.github.io/adk-docs/) that simulates a school coordinator routing student questions to specialized teacher agents.

## Architecture

```
school_coordinator_agent (root - Gemini 2.5 Flash)
├── english_teacher_agent (Gemini 2.0 Flash)
├── maths_teacher_agent (Gemini 2.0 Flash) — with calculator tool
├── science_teacher_agent (Gemini 2.0 Flash)
├── history_teacher_agent (Gemini 2.0 Flash)
├── geography_teacher_agent (Gemini 2.0 Flash)
└── computerscience_teacher_agent (Gemini 2.0 Flash) — with google search tool
```

## How It Works

The **School Coordinator** is the root agent that receives all user messages and routes them to the appropriate teacher agent based on the subject:

| Subject | Agent | Tools |
|---------|-------|-------|
| English, grammar, literature, creative writing | english_teacher_agent | — |
| Maths, calculations, algebra, geometry | maths_teacher_agent | calculator |
| Science, physics, chemistry, biology | science_teacher_agent | — |
| History, historical events, civilizations | history_teacher_agent | — |
| Geography, countries, maps, continents, physical features | geography_teacher_agent | — |
| Computer science, programming, algorithms, data structures, networking | computerscience_teacher_agent | google_search |

If the user's question doesn't clearly match a subject, the coordinator responds directly.

## Features

- **Multi-agent routing** — Coordinator intelligently delegates to subject-specific agents
- **Tool usage** — Maths agent has a calculator for accurate computations; CS agent can search the web for current information
- **Conversation memory** — Session-based history maintained across turns via ADK sessions (stored in `.adk/session.db`)

## Prerequisites

- Python 3.12+
- A [Google AI API key](https://aistudio.google.com/apikey)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kovurugopi/SchoolMultiAgent.git
   cd SchoolMultiAgent
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install google-adk
   ```

3. Create the `.env` file at `school_coordinator_agent/.env`:
   ```
   GOOGLE_GENAI_USE_VERTEXAI=0
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Run the dev server (from the project root):
   ```bash
   adk web
   ```

5. Open http://127.0.0.1:8000 in your browser, select `school_coordinator_agent`, and start chatting.

## Example Usage

- "What is the capital of France?" → routed to geography agent
- "Calculate sqrt(144) + 25" → routed to maths agent (uses calculator tool)
- "Explain recursion in Python" → routed to computer science agent
- "Who was Alexander the Great?" → routed to history agent
- "What is photosynthesis?" → routed to science agent
- "Write a haiku about rain" → routed to english agent

## Project Structure

```
SchoolMultiAgent/
├── school_coordinator_agent/
│   ├── __init__.py
│   ├── agent.py                              # Root coordinator agent
│   ├── .env                                  # API keys (not committed)
│   ├── english_teacher_agent/
│   │   ├── __init__.py
│   │   └── english_agent.py
│   ├── maths_teacher_agent/
│   │   ├── __init__.py
│   │   └── maths_agent.py                   # Includes calculator tool
│   ├── science_teacher_agent/
│   │   ├── __init__.py
│   │   └── science_agent.py
│   ├── history_teacher_agent/
│   │   ├── __init__.py
│   │   └── history_agent.py
│   ├── geography_teacher_agent/
│   │   ├── __init__.py
│   │   └── geography_agent.py
│   └── computerscience_teacher_agent/
│       ├── __init__.py
│       └── computer_science_agent.py         # Includes google_search tool
├── .gitignore
└── README.md
```

## Built With

- [Google ADK](https://google.github.io/adk-docs/) — Agent Development Kit
- [Gemini 2.5 Flash](https://ai.google.dev/) — LLM powering the coordinator
- [Gemini 2.0 Flash](https://ai.google.dev/) — LLM powering the sub-agents
