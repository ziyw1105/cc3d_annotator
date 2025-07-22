from crewai import Agent

CodeDividerAgent = Agent(
    role="Code Divider",
    goal="Divide code into cell types, functions, and biomedical context",
    backstory="You understand how biological simulations are structured.",
    verbose=True,
    allow_delegation=False
)
