from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/jobs", response_model=List[schemas.Job])
def get_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
	users = crud.get_jobs(db, skip=skip, limit=limit)
	return users

@app.post("/jobs",response_model=schemas.Job)
def create_jobs(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_jobs(db=db, job=job)

@app.delete("/jobs/{job_id}", response_model=schemas.Status)
def delete_jobs(job_id : int, db: Session = Depends(get_db)):
	delete_status = crud.delete_job(db=db, job_id=job_id)
	if delete_status:
		return schemas.Status(message=f"Deleted job {job_id}")
	return schemas.Status(message=f"Job {job_id} not found")

@app.post("/jobs/{job_id}",response_model=schemas.Job)
def get_details_by_id(job_id : int, db: Session = Depends(get_db)):
    return crud.get_job_by_id(db=db, job_id=job_id)


@app.post("/jobs/{job_id}/apply",response_model=schemas.Status)
def apply_for_job(job_id : int, db: Session = Depends(get_db)):
	job_data =crud.get_job_by_id(db=db,job_id=job_id)
	if job_data:
		return schemas.Status(message=f"Applyed for job {job_id}")
	return schemas.Status(message=f"Job {job_id} not found")



	