"""
Research Stage 2 execution with dependency management.
Researcher 1 completes Stage 2 first, then Researcher 2 updates based on those findings.
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


def create_summary_file(researcher_name: str, stage: str, findings: str, output_dir: Path) -> Path:
    """Create a markdown summary file for research findings."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{researcher_name.replace(' ', '_')}_{stage}_findings.md"
    filepath = output_dir / filename

    content = f"""# {researcher_name} - {stage} Findings

**Generated:** {Path(str(Path.cwd())).name}

## Overview

{findings[:1000]}

---

## Full Report

{findings}

---

*This report was generated using the Anthropic Claude Opus 4.1 model.*
"""

    filepath.write_text(content, encoding="utf-8")
    return filepath


def main() -> None:
    """Run Researcher 1 Stage 2, then Researcher 2 Stage 2 with dependency."""
    print("WasteProcessing - Research Stage 2\n")

    researcher_1_stage2_findings = run_researcher(
        db_path=DATA_PATH,
        researcher_name="Researcher 1 - Stage 2",
        mission="Refine the toilet-level waste processing designs with focus on practical implementation.",
        scope=[
            "Provide 3 refined solutions (down from 5) for toilet-level waste processing",
            "Separation of liquids and solids with liquids exiting first",
            "Reduce liquid content in solids by 20% (instead of 50%)",
            "Preliminary treatment of liquids for reuse in toilet flushing",
            "No smell or discoloration of treated reuse liquids",
            "Use basic compression mechanisms (coffee plunger, corkscrew analogs)",
            "Exclude chemicals and heating solutions",
            "Show retrofitting details for existing toilets where possible",
        ],
        deliverables=[
            "3 refined design concepts with liquid/solid separation",
            "Detailed compression mechanism specifications",
            "Liquid treatment and reuse process description",
            "Installation and retrofitting guidance",
            "Cost and complexity assessment for each design",
        ],
    )

    researcher_1_file = create_summary_file(
        "Researcher_1", "Stage_2", researcher_1_stage2_findings, RESEARCH_NOTES
    )
    print(f"\n✓ Researcher 1 Stage 2 summary saved: {researcher_1_file}\n")

    researcher_2_stage2_findings = run_researcher(
        db_path=DATA_PATH,
        researcher_name="Researcher 2 - Stage 2",
        mission="Update UK waste management sector analysis based on refined toilet-level waste reduction solutions from Researcher 1.",
        scope=[
            "Review and incorporate Researcher 1 Stage 2 solutions into economic analysis",
            "Update cost figures based on refined designs (3 solutions instead of 5)",
            "Detailed investigation of pollution incident costs: cleanup, loss of usage, tourism impact",
            "Analysis of benefits from reducing pollution incidents",
            "Cost to UK taxpayers for maintaining regulatory bodies and investigations",
            "Research AI predictive maintenance solutions for waste facilities",
            "Update all figures to 2024-2025 data (from previous 2023 baseline)",
            "Scenario modeling for toilet-level waste reduction impact on infrastructure costs",
        ],
        deliverables=[
            "Updated market analysis incorporating Stage 2 designs",
            "Detailed pollution incident cost breakdown",
            "Economic impact of pollution reduction",
            "Regulatory and enforcement cost analysis",
            "AI predictive maintenance landscape and potential savings",
            "2024-2025 financial and operational projections",
        ],
    )

    researcher_2_file = create_summary_file(
        "Researcher_2", "Stage_2", researcher_2_stage2_findings, RESEARCH_NOTES
    )
    print(f"\n✓ Researcher 2 Stage 2 summary saved: {researcher_2_file}\n")

    print(f"\n{'='*80}")
    print("Research Stage 2 Complete")
    print(f"{'='*80}")
    print(f"Researcher 1 Stage 2: {researcher_1_file}")
    print(f"Researcher 2 Stage 2: {researcher_2_file}")
    print(f"\nAll findings stored in: {DATA_PATH}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
