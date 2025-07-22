from crewai import Agent

EvaluatorAgent = Agent(
    role="Evaluator",
    goal="Evaluate the consistency and completeness of annotations",
    backstory="You ensure correctness in ontology and biological relevance.",
    verbose=True,
    allow_delegation=False
)
