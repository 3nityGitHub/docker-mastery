
---
# Talium Care Management App — Production Stack

This repository contains the full Dockerized backend stack for the **Talium Care Management App**. A new engineer should be able to clone the repo, configure environment variables, and run the entire stack locally using this documentation alone.

## 🚀 Tech Stack
- Flask (Python backend API)
- PostgreSQL (Primary database)
- Redis (Caching + background task support)
- Docker & Docker Compose (Container orchestration)

## 📦 Project Structure

.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .dockerignore
├── README.md
└── initdb/
    └── init.sql

## 🔧 Prerequisites
Ensure the following are installed:
- Docker
- Docker Compose
- Git
- Python 3.10+ (only required if running the app outside Docker)

## 🛠️ Setup Instructions

### 1️⃣   Clone the repository
```bash
git clone <REPO_URL>
cd <REPO_NAME>

2️⃣  Create your `.env` file
cp .env.example .env

Update values as needed:
POSTGRES_USER=talium
POSTGRES_PASSWORD=talium_password
POSTGRES_DB=talium_db
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379

3️⃣ Build and start the stack
docker compose up --build -d

4️⃣ Verify containers are running
docker compose ps

Expected:
app — healthy
db — healthy
redis — running
If any service is not healthy:
docker logs app
docker logs db
docker logs redis

🧪 Testing the API
Backend is available at:
http://localhost:5000

Test health endpoint:
curl http://localhost:5000/health

Expected:
{"status":"healthy"}

🗄️ Database Access
docker exec -it db psql -U talium -d talium_db

🧹 Stopping the Stack
docker compose down

Remove volumes (⚠️ deletes all data):
docker compose down -v

🛠️ Development Workflow
Rebuild after code changes:
docker compose up --build -d

View logs:
docker compose logs -f app

📁 Adding New Python Dependencies
Add the package to app/requirements.txt
Rebuild:
docker compose up --build -d

🧩 Common Issues
❌ Database connection error
Fix: Ensure .env values match service names.
❌ Flask app not starting
Fix: Check app.py for syntax errors and rebuild.
❌ Redis connection refused
Fix: Ensure Redis container is running:
docker compose ps


---
