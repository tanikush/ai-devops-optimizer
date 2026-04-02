from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "AI DevOps Pipeline Optimizer"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/devops_optimizer"
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_PASSWORD: str = ""
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-change-this"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # ML Models
    MODEL_PATH: str = "./ml-pipeline/models"
    MODEL_VERSION: str = "v1"
    PREDICTION_THRESHOLD: float = 0.7
    
    # CI/CD Integrations
    GITHUB_TOKEN: str = ""
    GITHUB_WEBHOOK_SECRET: str = ""
    GITLAB_TOKEN: str = ""
    GITLAB_URL: str = "https://gitlab.com"
    JENKINS_URL: str = ""
    JENKINS_USERNAME: str = ""
    JENKINS_PASSWORD: str = ""
    
    # Monitoring
    ENABLE_METRICS: bool = True
    METRICS_PORT: int = 9090
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        # Ignore extra fields from .env
        extra = "ignore"

# Create settings instance
settings = Settings()

# CORS origins - hardcoded for simplicity
CORS_ORIGINS = ["http://localhost:3000", "http://localhost:3001", "http://localhost:8000", "*"]
