# DevOps Microservice Starter Kit

A production-ready microservice boilerplate featuring a FastAPI REST API, Docker multi-container orchestration, and automated GitHub Actions CI testing and container building.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD Pipeline
├── app/
│   ├── main.py                # FastAPI Application & Endpoints
│   └── test_main.py           # Automated Unit & Integration Tests
├── Dockerfile                 # Hardened, Non-Root Container Definition
├── docker-compose.yml         # Multi-Container Deployment (Web + Redis)
├── .dockerignore              # Excluded Build Artifacts
├── .gitignore                 # Excluded Git Files
├── requirements.txt           # Python Dependencies
└── README.md                  # Instructions
```

## Quick Start Guide

### 1. Run Locally with Python & Pytest
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run unit tests
pytest -v app/test_main.py

# Launch development server
uvicorn app.main:app --reload --port 8000
```
Access app at `http://localhost:8000` and health check at `http://localhost:8000/health`.

---

### 2. Run with Docker
```bash
# Build Docker Image
docker build -t devops-sample-app:1.0.0 .

# Run Container
docker run -d -p 8000:8000 --name my-app devops-sample-app:1.0.0

# Check Health Endpoint
curl http://localhost:8000/health
```

---

### 3. Run Stack with Docker Compose
```bash
# Launch FastAPI + Redis stack in detached mode
docker-compose up -d

# Check running services
docker-compose ps

# View live logs
docker-compose logs -f web

# Stop stack and remove volumes
docker-compose down -v
```

---

### 4. Continuous Integration Pipeline
Pushing code or opening a Pull Request against `main` triggers `.github/workflows/ci.yml` which:
1. Installs dependencies and runs `pytest` test suite.
2. Sets up Docker Buildx with layer caching (`gha`).
3. Builds the production image and verifies health status.
