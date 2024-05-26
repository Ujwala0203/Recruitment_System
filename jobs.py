from bson import ObjectId # type: ignore
from fastapi import APIRouter, Depends, HTTPException

from models.models.py import Job # type: ignore
from services.database import jobs_collection # type: ignore

router = APIRouter()

@router.get("/")
async def view_jobs():
    jobs = await jobs_collection.find().to_list(1000)
    return jobs

@router.post("/")
async def post_job(job: Job):
    job_dict = job.dict()
    job_dict["_id"] = str(ObjectId())
    await jobs_collection.insert_one(job_dict)
    return {"message": "Job posted successfully"}

@router.put("/{job_id}")
async def update_job(job_id: str, job: Job):
    job_dict = job.dict()
    result = await jobs_collection.update_one({"_id": job_id}, {"$set": job_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Job updated successfully"}

@router.put("/{job_id}/status")
async def update_job_status(job_id: str, status: str):
    result = await jobs_collection.update_one({"_id": job_id}, {"$set": {"status": status}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Job status updated successfully"}
