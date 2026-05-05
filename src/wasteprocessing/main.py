import os
from pathlib import Path
from dotenv import load_dotenv

from wasteprocessing.agents import get_agent_roles
from wasteprocessing.database import init_db, summarize_reports

ROOT = Path(__file__).resolve().parent.parent
GLOBAL_ENV = Path.home() / ".env"
LOCAL_ENV = ROOT / ".env"
DATABASE_PATH = ROOT / "data" / "waste_research.db"

load_dotenv(GLOBAL_ENV, override=False)
load_dotenv(LOCAL_ENV, override=True)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


def main() -> None:
    print("WasteProcessing project scaffold")
    print("Repository root:", ROOT)

    if ANTHROPIC_API_KEY is None:
        print("Warning: ANTHROPIC_API_KEY is not set. Ensure ~/.env contains MYAPI and the local .env references it.")
    else:
        print("Anthropic API key loaded from environment.")

    init_db(DATABASE_PATH)
    print(f"Database initialized at {DATABASE_PATH}")

    print("\nAvailable agent roles:")
    for role in get_agent_roles():
        print(f"- {role.name}: {role.focus}")

    print("\nUse the `agents/` directory to capture structured research tasks and the `data/` folder for saved report data.")


if __name__ == "__main__":
    main()
