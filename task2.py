from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptInput(BaseModel):
    project: str
    skills: List[str]

@app.post("/build-prompt")
def build_prompt(data: PromptInput):

    prompt = f"""Generate ATS friendly bullet points.

Project:
{data.project}

Skills:
{", ".join(data.skills)}
"""

    return {
        "prompt": prompt
    }