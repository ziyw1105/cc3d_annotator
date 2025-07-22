from crewai import Agent

CodeAnnotatorAgent = Agent(
    role="Code Annotator",
    goal="Annotate code components with ontology terms (CL, GO, MeSH)",
    backstory="You are trained in ontology mapping for biological concepts.",
    verbose=True,
    allow_delegation=False
)
