from bson import ObjectId # type: ignore
from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr

from models.models.py import Candidate # type: ignore
from services.database import candidates_collection, resumes_collection # type: ignore

router = APIRouter()

@router.post("/signup")
async def signup(candidate: Candidate):
    candidate_dict = candidate.dict()
    existing_candidate = await candidates_collection.find_one({"email": candidate.email})
    if existing_candidate:
        raise HTTPException(status_code=400, detail="Email already registered")
    candidate_dict["_id"] = str(ObjectId())
    await candidates_collection.insert_one(candidate_dict)
    return {"message": "Candidate registered successfully"}

@router.post("/login")
async def login(email: EmailStr, password: str):
    candidate = await candidates_collection.find_one({"email": email})
    if not candidate or candidate["password"] != password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {"message": "Login successful", "candidate_id": candidate["_id"]}

@router.post("/apply/{job_id}")
async def apply_for_job(candidate_id: str, job_id: str):
    candidate = await candidates_collection.find_one({"_id": candidate_id})
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    job = await jobs_collection.find_one({"_id": job_id}) # type: ignore
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    # Here you might want to add the job_id to the candidate's list of applications
    return {"message": "Applied for job successfully"}

@router.post("/upload_resume")
async def upload_resume(candidate_id: str, resume_file: str):
    candidate = await candidates_collection.find_one({"_id": candidate_id})
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    resume = {"candidate_id": candidate_id, "resume_file": resume_file}
    resume["_id"] = str(ObjectId())
    await resumes_collection.insert_one(resume)
    return {"message": "Resume uploaded successfully"}
