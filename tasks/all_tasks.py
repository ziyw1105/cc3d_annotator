from crewai import Task
from agents.model_reformer import ModelReformerAgent
from agents.context_extractor import ContextExtractorAgent
from agents.code_divider import CodeDividerAgent
from agents.code_annotator import CodeAnnotatorAgent
from agents.parameter_annotator import ParameterAnnotatorAgent
from agents.evaluator import EvaluatorAgent
from agents.correlation_agent import CorrelationAgent
from agents.report_generator import ReportGeneratorAgent

ReformCodeTask = Task(
    description="Clean up model.py and model.xml by removing commented code and unused imports.",
    expected_output="Cleaned Python and XML code without clutter.",
    agent=ModelReformerAgent
)

ExtractContextTask = Task(
    description="Read and summarize the research abstract to extract relevant biological context.",
    expected_output="A concise summary with extracted biological keywords and topics.",
    agent=ContextExtractorAgent
)

DivideCodeTask = Task(
    description="Separate the code into sections: cell types, biological functions, biomedical context.",
    expected_output="Labeled sections of code based on CL, GO, and MeSH mappings.",
    agent=CodeDividerAgent
)

AnnotateCodeTask = Task(
    description="Annotate each section of code with the appropriate ontology terms (CL, GO, MeSH).",
    expected_output="Annotated code blocks with ontology references and reasoning.",
    agent=CodeAnnotatorAgent
)

AnnotateParamsTask = Task(
    description="Identify simulation parameters and explain their biological significance.",
    expected_output="Parameter list with biological relevance, units, and ontology mappings if possible.",
    agent=ParameterAnnotatorAgent
)

EvaluateAnnotationsTask = Task(
    description="Review all annotations for accuracy, completeness, and consistency across all components.",
    expected_output="Evaluation report summarizing any inconsistencies, gaps, or improvement suggestions.",
    agent=EvaluatorAgent
)

CorrelateAndRefineTask = Task(
    description="Relate simulation behaviors to biological functions and cell types, refining annotations based on behavioral cues.",
    expected_output="Correlated insights between behavior and ontology-mapped biological functions.",
    agent=CorrelationAgent
)

GenerateReportTask = Task(
    description="Generate a structured JSON report compiling all annotated entities, parameters, behaviors, and context.",
    expected_output="Comprehensive annotation report in JSON format for downstream analysis.",
    agent=ReportGeneratorAgent
)
