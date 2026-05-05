import os
from pathlib import Path

import anthropic

from wasteprocessing.database import Report, save_report


def run_researcher(
    db_path: Path,
    researcher_name: str,
    mission: str,
    scope: list[str],
    deliverables: list[str],
) -> str:
    """
    Execute a research task using the Anthropic API.
    
    Args:
        db_path: Path to the SQLite database for storing results.
        researcher_name: Name of the researcher (e.g., "Researcher 1").
        mission: The research mission statement.
        scope: List of scope items to research.
        deliverables: Expected deliverables.
    
    Returns:
        The research findings as a string.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY is not set in the environment.")

    client = anthropic.Anthropic(api_key=api_key)

    scope_text = "\n".join(f"- {item}" for item in scope)
    deliverables_text = "\n".join(f"{i}. {item}" for i, item in enumerate(deliverables, 1))

    prompt = f"""You are {researcher_name}, a specialized research agent for the WasteProcessing project.

Your mission:
{mission}

Your research scope:
{scope_text}

Expected deliverables:
{deliverables_text}

Conduct thorough, structured research on this topic. Provide detailed findings, data points, and actionable insights. Be specific with numbers, references, and technical details where possible. Structure your response clearly with sections for each deliverable.

Begin your research now:"""

    print(f"\n{'='*80}")
    print(f"Starting {researcher_name}...")
    print(f"{'='*80}\n")

    findings = ""
    with client.messages.stream(
        model="claude-opus-4-1-20250805",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            findings += text
            print(text, end="", flush=True)

    print(f"\n\n{'='*80}")
    print(f"{researcher_name} research complete.")
    print(f"{'='*80}\n")

    report = Report(
        agent=researcher_name,
        category="research_findings",
        title=f"{researcher_name} - {mission.split()[0:3]}",
        summary=findings[:500],
        details=findings,
        source="Anthropic API Claude Research",
    )
    save_report(db_path, report)

    return findings
