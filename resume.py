from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Resume(BaseModel):
    name: str
    email: str
    phone: str
    skills: list[str]
    education: str
    experience: str

@app.post("/generate-resume")
def generate_resume(data: Resume):

    resume = f"""
==================================================
                {data.name.upper()}
==================================================

📧 Email : {data.email}
📱 Phone : {data.phone}

--------------------------------------------------
PROFESSIONAL SUMMARY
--------------------------------------------------
Motivated professional with expertise in
{', '.join(data.skills)} and a strong interest in
continuous learning and career growth.

--------------------------------------------------
EDUCATION
--------------------------------------------------
{data.education}

--------------------------------------------------
WORK EXPERIENCE
--------------------------------------------------
{data.experience}

--------------------------------------------------
TECHNICAL SKILLS
--------------------------------------------------
"""

    for skill in data.skills:
        resume += f"\n• {skill}"

    resume += """

--------------------------------------------------
DECLARATION
--------------------------------------------------
I hereby declare that the above information is
true and correct to the best of my knowledge.

Signature
____________________
"""

    return {
        "message": "Resume Generated Successfully",
        "resume": resume
    }