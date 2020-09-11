from sqlalchemy.orm import Session

import models, schemas

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()

def create_jobs(db: Session, job: schemas.JobCreate):
    db_item = models.Job(title=job.title,description=job.description,company=job.company)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_job_by_id(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def delete_job(db: Session, job_id: int):
    job = db.query(models.Job).filter(models.Job.id == job_id).delete()
    db.commit() 
    return job

def apply_for_job(db: Session, job_id: schemas.ApplicationBase):
    db_item = models.Application(job_id = job_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
