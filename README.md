# WasteProcessing

This repository is the initial scaffold for the WasteProcessing research initiative.
The project focuses on UK human waste management, including toilet-level separation and dehydration concepts, UK sector analysis, and investment presentation research.

## Project Goals

- Research toilet-based human waste processing that can reduce solid weight/volume by ~50%.
- Collect structured research data for later extraction and analysis.
- Build agent-driven workflows for:
  - Researcher 1: toilet system design and waste separation
  - Researcher 2: UK waste management sector and economics
  - Presentation specialist: investor-ready summaries and recommendations

## Setup

1. Install Python 3.11+.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .
   ```
3. Ensure your global Anthropic key is available in `~/.env` with `MYAPI=<your-key>`.
4. The local `.env` is configured to reference the global key:
   ```bash
   ANTHROPIC_API_KEY=${MYAPI}
   ```
5. All `.env` files are ignored by git; the committed `.env.example` is the template.

## Project Structure

- `agents/` – research agent task definitions and responsibilities.
- `docs/` – architecture, workflows, and research plans.
- `src/wasteprocessing/` – project core code for environment loading, database setup, and agent scaffolding.
- `InitialProjectOverview.md` – original user project overview and goals.

## Usage

Run the project entrypoint:
```bash
python -m wasteprocessing
```

The project is designed as a collaboration workspace for research, not a finished product. The Python modules demonstrate how to load environment configuration, initialize a structured local database, and keep agent roles documented.
