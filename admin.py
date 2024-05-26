from fastapi import APIRouter, HTTPException
from models.models.py import Candidate, Resume, Job # type: ignore
from services.database import candidates_collection, resumes_collection # type: ignore

router = APIRouter()

@router.post("/login")
async def admin_login(email: str, password: str):
    # Implement admin login logic
    return {"message": "Admin login successful"}

@router.get("/candidates")
async def view_candidates():
    candidates = await candidates_collection.find().to_list(1000)
    return candidates

@router.get("/resumes")
async def view_resumes():
    resumes = await resumes_collection.find().to_list(1000)
    return resumes
