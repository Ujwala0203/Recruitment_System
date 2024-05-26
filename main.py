from fastapi import FastAPI  # type: ignore
from routes import admin, candidate, jobs  # type: ignore

app = FastAPI()

app.include_router(candidate.router, prefix="/candidate")
app.include_router(admin.router, prefix="/admin")
app.include_router(jobs.router, prefix="/jobs")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recruitment System"}

