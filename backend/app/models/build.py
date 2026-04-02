from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class Build(Base):
    __tablename__ = "builds"
    
    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"), nullable=False)
    build_number = Column(Integer, nullable=False)
    
    # Status
    status = Column(String, nullable=False)  # success, failed, running, pending, cancelled
    
    # Timing
    duration = Column(Float)  # in seconds
    started_at = Column(DateTime)
    finished_at = Column(DateTime)
    
    # Git Info
    commit_sha = Column(String)
    branch = Column(String)
    author = Column(String)
    commit_message = Column(Text)
    
    # Build Info
    trigger = Column(String)  # push, pull_request, manual, scheduled
    logs_url = Column(String)
    
    # Predictions
    predicted_status = Column(String)
    predicted_duration = Column(Float)
    prediction_confidence = Column(Float)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    pipeline = relationship("Pipeline", back_populates="builds")
    metrics = relationship("Metric", back_populates="build", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Build(id={self.id}, pipeline_id={self.pipeline_id}, build_number={self.build_number}, status={self.status})>"
