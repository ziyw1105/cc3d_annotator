from crewai import Agent

ContextExtractorAgent = Agent(
    role="Context Extractor",
    goal="Extract context and key biological terms from abstracts",
    backstory="You are skilled at summarizing scientific research for code interpretation.",
    verbose=True,
    allow_delegation=False
)
