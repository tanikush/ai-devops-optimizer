# Setup Guide

## Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher
- PostgreSQL 13 or higher
- Redis 6 or higher
- Docker and Docker Compose (optional)

## Local Development Setup

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
copy .env.example .env

# Edit .env with your configuration
# Update DATABASE_URL, REDIS_URL, etc.

# Run database migrations (if using Alembic)
alembic upgrade head

# Start the backend server
python -m app.main
```

The backend will be available at http://localhost:8000

API Documentation: http://localhost:8000/docs

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
copy .env.example .env

# Edit .env with your configuration

# Start the development server
npm run dev
```

The frontend will be available at http://localhost:3000

### 3. Database Setup

```bash
# Create PostgreSQL database
createdb devops_optimizer

# Or using psql
psql -U postgres
CREATE DATABASE devops_optimizer;
```

### 4. Redis Setup

Make sure Redis is running:

```bash
# On Windows (if installed)
redis-server

# On macOS
brew services start redis

# On Linux
sudo systemctl start redis
```

## Docker Setup

The easiest way to run the entire application:

```bash
cd infrastructure/docker
docker-compose up -d
```

This will start:
- PostgreSQL database on port 5432
- Redis on port 6379
- Backend API on port 8000
- Frontend on port 3000

## Environment Variables

### Backend (.env)

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/devops_optimizer
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key-here
GITHUB_TOKEN=your-github-token
```

### Frontend (.env)

```
VITE_API_BASE_URL=http://localhost:8000
```

## Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running
- Check DATABASE_URL in .env
- Verify database exists

### Redis Connection Issues

- Ensure Redis is running
- Check REDIS_URL in .env

### Port Already in Use

- Change ports in .env or docker-compose.yml
- Kill processes using the ports

## Next Steps

1. Configure CI/CD integrations (GitHub, Jenkins, etc.)
2. Train ML models with your pipeline data
3. Set up monitoring and alerts
4. Configure authentication if needed

For more information, see the main README.md
