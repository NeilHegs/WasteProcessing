from dataclasses import dataclass
from typing import List


@dataclass
class AgentRole:
    name: str
    focus: str
    deliverables: List[str]


def get_agent_roles() -> List[AgentRole]:
    return [
        AgentRole(
            name="Researcher 1",
            focus="toilet-level waste processing and separation within existing toilet form factors",
            deliverables=[
                "Five initial design concepts",
                "Comparison of installation difficulty, cost, noise, and readiness time",
                "Options for liquid filtration and local reuse",
            ],
        ),
        AgentRole(
            name="Researcher 2",
            focus="UK human waste management sector research, costs, and technology trends",
            deliverables=[
                "Industry pain points and financial drivers",
                "Transportation and facility processing cost analysis",
                "Impact assessment for 50% solid waste reduction in toilets",
            ],
        ),
        AgentRole(
            name="Presentation Specialist",
            focus="investor presentation and executive summary for first-round meetings",
            deliverables=[
                "Overview of UK waste management issues",
                "Cost-benefit narrative for toilet-level waste reduction",
                "Structured slide outline for investor review",
            ],
        ),
    ]
