from crewai import Agent

ModelReformerAgent = Agent(
    role="Model Reformer",
    goal="Clean and simplify the CC3D code by removing irrelevant or unused sections",
    backstory="You're a code cleaner expert, especially for biological simulation models.",
    verbose=True,
    allow_delegation=False
)
