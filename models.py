from datetime import date
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class Candidate(BaseModel):
    id: Optional[str]  # MongoDB will generate this automatically
    name: str
    email: EmailStr
    password: str

class Job(BaseModel):
    id: Optional[str]
    title: str
    description: str
    department: str
    location: str
    employment_type: str
    salary_range: Optional[str]
    application_deadline: Optional[date]
    required_skills: List[str]
    additional_info: Optional[str]
    status: str  # e.g., "Open", "Closed", "Filled"

class Resume(BaseModel):
    id: Optional[str]
    candidate_id: str  # Reference to the candidate
    resume_file: str  # Path to the resume file
