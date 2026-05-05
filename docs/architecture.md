# WasteProcessing Architecture

This project is designed to support structured research and agent-driven workflows for human waste management in the UK.

## Core Concepts

- `src/wasteprocessing/` contains the application entrypoint, database plumbing, and agent role scaffolding.
- `agents/` contains the initial task definitions for the three focused agents.
- `data/` is reserved for the SQLite research database and any generated outputs.
- `.env` is intentionally configured to reference the global Anthropic API key stored in `~/.env`.

## Environment

The local `.env` file contains:

```bash
ANTHROPIC_API_KEY=${MYAPI}
```

This allows the project to load the global key from `~/.env` while keeping repository secrets out of version control.

## Data Storage

The repository uses a lightweight SQLite database schema for structured research reports.
The table layout is currently:
- `reports(id, agent, category, title, summary, details, source, created_at)`

## Agent Workflow

- Researcher 1: toilet design and waste separation
- Researcher 2: UK waste sector and cost analysis
- Presentation Specialist: investor narrative and slide structure

The goal is to capture findings in a structured way that can later be queried or exported for reporting and presentation.
