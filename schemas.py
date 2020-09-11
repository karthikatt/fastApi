from typing import List, Optional

from pydantic import BaseModel

class Status(BaseModel):
    message: str

class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    company: str


class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    title: str
    is_active: bool

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    job_id: str

class Application(ApplicationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
