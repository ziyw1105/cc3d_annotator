# -*- coding: utf-8 -*-
from crewai import Crew
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load API keys from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Import all tasks (and their agents are included with them)
from tasks.all_tasks import (
    ReformCodeTask,
    ExtractContextTask,
    DivideCodeTask,
    AnnotateCodeTask,
    AnnotateParamsTask,
    EvaluateAnnotationsTask,
    CorrelateAndRefineTask,
    GenerateReportTask
)


# Instantiate the Crew
crew = Crew(
    agents=[
        ReformCodeTask.agent,
        ExtractContextTask.agent,
        DivideCodeTask.agent,
        AnnotateCodeTask.agent,
        AnnotateParamsTask.agent,
        EvaluateAnnotationsTask.agent,
        CorrelateAndRefineTask.agent,
        GenerateReportTask.agent
    ],
    tasks=[
        ReformCodeTask,
        ExtractContextTask,
        DivideCodeTask,
        AnnotateCodeTask,
        AnnotateParamsTask,
        EvaluateAnnotationsTask,
        CorrelateAndRefineTask,
        GenerateReportTask
    ],
    memory=True,
    verbose=True
)

if __name__ == "__main__":
    print(" Running CrewAI for CC3D model annotation...")
    result = crew.kickoff()
    print("\n Final Result:\n")
    print(result)
