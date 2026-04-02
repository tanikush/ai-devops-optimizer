from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class Metric(Base):
    __tablename__ = "metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey("builds.id"), nullable=False)
    
    # Metric details
    metric_name = Column(String, nullable=False)  # cpu_usage, memory_usage, test_count, etc.
    metric_value = Column(Float, nullable=False)
    metric_unit = Column(String)  # percentage, MB, count, seconds
    
    # Stage information
    stage = Column(String)  # build, test, deploy
    
    # Timestamp
    recorded_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    build = relationship("Build", back_populates="metrics")
    
    def __repr__(self):
        return f"<Metric(id={self.id}, name={self.metric_name}, value={self.metric_value})>"
