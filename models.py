from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String, index = True)
    company = Column(String, default = 1)
    is_active = Column(Boolean, default = True)
    applications = relationship("Application", back_populates="job")


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, default = 1)
    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship("Job", back_populates="applications")

