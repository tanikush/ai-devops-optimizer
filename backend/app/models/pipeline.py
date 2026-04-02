from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class Pipeline(Base):
    __tablename__ = "pipelines"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    platform = Column(String, nullable=False)  # github, jenkins, gitlab, circleci
    repository = Column(String)
    branch = Column(String, default="main")
    status = Column(String, default="active")  # active, inactive, archived
    
    # Metrics
    total_runs = Column(Integer, default=0)
    success_rate = Column(Float, default=0.0)
    avg_duration = Column(Float, default=0.0)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_run_at = Column(DateTime)
    
    # Configuration
    config = Column(String)  # JSON string
    
    # Relationships
    builds = relationship("Build", back_populates="pipeline", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Pipeline(id={self.id}, name={self.name}, platform={self.platform})>"
