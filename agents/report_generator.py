from crewai import Agent

ReportGeneratorAgent = Agent(
    role="Report Generator",
    goal="Generate a structured JSON summary of all annotations",
    backstory="You compile detailed annotation reports for downstream use.",
    verbose=True,
    allow_delegation=False
)
