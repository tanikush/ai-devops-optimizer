from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from datetime import datetime
from app.database.session import Base

class Recommendation(Base):
    __tablename__ = "recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"), nullable=False)
    
    # Recommendation details
    type = Column(String, nullable=False)  # performance, caching, resource, testing
    priority = Column(String, nullable=False)  # high, medium, low
    title = Column(String, nullable=False)
    description = Column(Text)
    
    # Impact estimates
    estimated_time_saved = Column(Float)  # in seconds
    estimated_cost_saved = Column(Float)  # in dollars
    implementation_effort = Column(String)  # low, medium, high
    
    # Status
    status = Column(String, default="pending")  # pending, applied, dismissed, expired
    applied_at = Column(DateTime)
    
    # Actual results (after application)
    actual_time_saved = Column(Float)
    actual_cost_saved = Column(Float)
    effectiveness = Column(Float)  # 0.0 to 1.0
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Recommendation(id={self.id}, pipeline_id={self.pipeline_id}, title={self.title})>"
