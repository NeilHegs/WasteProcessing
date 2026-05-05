"""
Research execution and summary generation for Researcher 1 and Researcher 2.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from wasteprocessing.research import run_researcher

ROOT = Path(__file__).resolve().parent
GLOBAL_ENV = Path.home() / ".env"
LOCAL_ENV = ROOT / ".env"
DATA_PATH = ROOT / "data" / "waste_research.db"
RESEARCH_NOTES = ROOT / "ResearchNotes"

load_dotenv(GLOBAL_ENV, override=False)
load_dotenv(LOCAL_ENV, override=True)


def create_summary_file(researcher_name: str, findings: str, output_dir: Path) -> Path:
    """Create a markdown summary file for research findings."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{researcher_name.replace(' ', '_')}_findings.md"
    filepath = output_dir / filename

    content = f"""# {researcher_name} - Research Findings

**Generated:** {Path(str(Path.cwd())).name}

## Overview

{findings[:1000]}

---

## Full Report

{findings}

---

*This report was generated using the Anthropic Claude 3.5 Sonnet model.*
"""

    filepath.write_text(content, encoding="utf-8")
    return filepath


def main() -> None:
    """Run both researchers and generate summary files."""
    print("WasteProcessing - Research Execution\n")

    researcher_1_findings = run_researcher(
        db_path=DATA_PATH,
        researcher_name="Researcher 1",
        mission="Research the design of toilet-level systems that can reduce solid waste volume/weight by approximately 50% while preserving the toilet's existing user-facing form and function.",
        scope=[
            "Human waste entering and leaving the toilet: faeces, urine, vomit",
            "Solid/liquid separation and timing of discharge",
            "Internal materials and coatings that reduce adhesion and improve discharge",
            "Possible dehydration or absorbent layers inside the toilet",
            "Liquid filtration with potential local reuse",
        ],
        deliverables=[
            "Five distinct design ideas",
            "Manufacturing and installation cost estimates",
            "Technical complexity analysis",
            "Noise and cycle-time assessment",
            "Liquid treatment and reuse strategies",
        ],
    )

    researcher_2_findings = run_researcher(
        db_path=DATA_PATH,
        researcher_name="Researcher 2",
        mission="Research the current UK human waste management sector, highlighting company economics, facility challenges, transportation costs, and regulatory pressures.",
        scope=[
            "Private-sector waste management economics in the UK",
            "Transportation and treatment facility costs",
            "Profit pressure versus infrastructure investment",
            "Environmental impacts and existing performance gaps",
            "New technologies or proposals that could shift the industry paradigm",
            "Effects of toilet-level solid waste reduction on downstream operations",
        ],
        deliverables=[
            "Current market issues and company performance analysis",
            "Cost breakdowns for transport and processing",
            "Environmental impact summary",
            "Technology and policy opportunities",
            "Scenario analysis for 50% toilet-level solid waste reduction",
        ],
    )

    researcher_1_file = create_summary_file("Researcher_1", researcher_1_findings, RESEARCH_NOTES)
    researcher_2_file = create_summary_file("Researcher_2", researcher_2_findings, RESEARCH_NOTES)

    print(f"\n{'='*80}")
    print("Research Summary Files Created")
    print(f"{'='*80}")
    print(f"Researcher 1: {researcher_1_file}")
    print(f"Researcher 2: {researcher_2_file}")
    print(f"\nAll findings also stored in: {DATA_PATH}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
