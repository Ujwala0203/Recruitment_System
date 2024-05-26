from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore

client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client.recruitment_system

candidates_collection = database.get_collection("candidates")
jobs_collection = database.get_collection("jobs")
resumes_collection = database.get_collection("resumes")

async def get_database():
    return database
