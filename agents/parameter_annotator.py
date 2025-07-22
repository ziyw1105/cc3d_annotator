from crewai import Agent

ParameterAnnotatorAgent = Agent(
    role="Parameter Annotator",
    goal="Extract and explain biological significance of simulation parameters",
    backstory="You specialize in translating parameter values into biological meaning.",
    verbose=True,
    allow_delegation=False
)
