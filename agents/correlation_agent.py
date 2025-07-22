from crewai import Agent

CorrelationAgent = Agent(
    role="Correlation Agent",
    goal="Correlate cell behaviors in simulation to ontology-mapped functions",
    backstory="You link model behavior to biological insights.",
    verbose=True,
    allow_delegation=False
)
