# Agent Smith

An AI agent that explores its own codebase and can answer questions about how it works.

## What it does

Agent runs in a loop with tools: reads files, checks directory structure, and looks up topics on Wikipedia. Ask it anything about the codebase and it'll investigate using those tools to give you answers.

## How to use

```bash
python main.py
```

Type your questions, press enter. Agent Smith responds. Repeat.

## Requirements

- Python environment with `agents`, `requests`, `python-dotenv`
- OpenAI API key in `.env`
- `tree` command installed
