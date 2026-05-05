"""
Focused research on DCPS design expansion with diagrams.
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


def create_summary_file(researcher_name: str, focus: str, findings: str, output_dir: Path) -> Path:
    """Create a markdown summary file for research findings."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{researcher_name.replace(' ', '_')}_{focus}_detailed.md"
    filepath = output_dir / filename

    content = f"""# {researcher_name} - {focus} Detailed Analysis

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
    """Run detailed DCPS design research."""
    print("WasteProcessing - DCPS Detailed Design Research\n")

    dcps_detailed_findings = run_researcher(
        db_path=DATA_PATH,
        researcher_name="Researcher 1 - DCPS Detailed",
        mission="Provide comprehensive technical details and diagrams for the Dual-Chamber Plunger Separator System (DCPS) design.",
        scope=[
            "Detailed mechanical specifications and tolerances",
            "Step-by-step operational sequence with timing",
            "Material specifications and corrosion resistance",
            "Detailed liquid treatment process flow",
            "Installation procedure with tools and safety considerations",
            "Maintenance schedule and procedures",
            "Failure modes and troubleshooting guide",
            "Performance metrics and testing protocols",
            "Create ASCII/text-based diagrams for all components",
            "Cross-sectional views and operational flow diagrams",
            "Bill of materials with suppliers",
            "Integration with existing toilet plumbing",
        ],
        deliverables=[
            "Complete technical specification document",
            "Detailed operational diagrams",
            "Installation and maintenance manuals",
            "Performance testing protocols",
            "Cost breakdown and manufacturing guidelines",
        ],
    )

    dcps_file = create_summary_file(
        "Researcher_1", "DCPS_Detailed", dcps_detailed_findings, RESEARCH_NOTES
    )
    print(f"\n✓ DCPS detailed analysis saved: {dcps_file}\n")

    print(f"\n{'='*80}")
    print("DCPS Detailed Research Complete")
    print(f"{'='*80}")
    print(f"DCPS Details: {dcps_file}")
    print(f"\nAll findings stored in: {DATA_PATH}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
