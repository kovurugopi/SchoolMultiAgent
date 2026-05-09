# School Multi-Agent System

A multi-agent system built with [Google ADK (Agent Development Kit)](https://google.github.io/adk-docs/) that simulates a school coordinator routing student questions to specialized teacher agents.

## Architecture

```
school_coordinator_agent (root)
├── english_teacher_agent
├── maths_teacher_agent (with calculator tool)
├── science_teacher_agent
├── history_teacher_agent
├── geography_teacher_agent
└── computerscience_teacher_agent (with google search tool)
```

## How It Works

The **School Coordinator** is the root agent that receives all user messages and routes them to the appropriate teacher agent based on the subject:

| Subject | Agent | Tools |
|---------|-------|-------|
| English, grammar, literature, creative writing | english_teacher_agent | — |
| Maths, calculations, algebra, geometry | maths_teacher_agent | calculator |
| Science, physics, chemistry, biology | science_teacher_agent | — |
| History, historical events, civilizations | history_teacher_agent | — |
| Geography, countries, maps, continents | geography_teacher_agent | — |
| Computer science, programming, algorithms | computerscience_teacher_agent | google_search |

## Features

- **Multi-agent routing** — Coordinator intelligently delegates to subject-specific agents
- **Tool usage** — Maths agent has a calculator; CS agent can search the web
- **Conversation memory** — Session-based history maintained across turns via ADK sessions

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install google-adk
   ```

2. Add your API key to `school_coordinator_agent/.env`:
   ```
   GOOGLE_GENAI_USE_VERTEXAI=0
   GOOGLE_API_KEY=your_api_key_here
   ```

3. Run the dev server:
   ```bash
   adk web
   ```

4. Open http://127.0.0.1:8000 in your browser and start chatting.

## Project Structure

```
SchoolMultiAgent/
├── school_coordinator_agent/
│   ├── __init__.py
│   ├── agent.py                          # Root coordinator agent
│   ├── .env                              # API keys (not committed)
│   ├── english_teacher_agent/
│   ├── maths_teacher_agent/
│   ├── science_teacher_agent/
│   ├── history_teacher_agent/
│   ├── geography_teacher_agent/
│   └── computerscience_teacher_agent/
├── .gitignore
└── README.md
```

## Built With

- [Google ADK](https://google.github.io/adk-docs/) — Agent Development Kit
- [Gemini 2.0 Flash](https://ai.google.dev/) — LLM powering the agents
