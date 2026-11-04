# 🥠 Fortune Cookie Web App

A small Flask web app that shows a random fortune on every refresh.
Built to demonstrate **Git, GitHub, Docker, GitHub Actions (CI/CD) and Docker Hub**.

| Route | What it does |
|---|---|
| `/` | Web page with a random fortune |
| `/api/fortune` | JSON API: `{"fortune": "..."}` |
| `/health` | Health check: `{"status": "ok"}` |

## Project structure

```
fortune-cookie/
├── app.py                      # Flask application
├── test_app.py                 # Automated tests (pytest)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Recipe to build the Docker image
├── .dockerignore               # Files Docker should not copy into the image
├── .gitignore                  # Files Git should not track
└── .github/workflows/
    └── ci-cd.yml               # GitHub Actions pipeline (test -> build -> push)
```

## Concepts

- **Git**: version control. Saves snapshots (commits) of your project.
- **GitHub**: cloud hosting for Git repositories.
- **Docker image**: read-only blueprint with the app, Python and dependencies.
- **Docker container**: a running instance of an image.
- **Dockerfile**: the recipe for building an image.
- **Docker Hub**: cloud registry for sharing images.
- **CI/CD**: Continuous Integration (auto-test every change) and Continuous Delivery (auto-build and publish).
- **GitHub Actions**: GitHub's cloud automation that runs CI/CD from a YAML file.

## Run locally (without Docker)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest
python app.py
```
Open http://localhost:5000

## Run with Docker

```bash
docker build -t fortune-cookie:1.0 .
docker run -d -p 8080:5000 --name fortune fortune-cookie:1.0
curl http://localhost:8080/api/fortune
docker logs fortune
docker stop fortune && docker rm fortune
```

## Git workflow

```bash
git init
git add .
git commit -m "Add fortune cookie Flask app with tests"
git branch -M main
git remote add origin https://github.com/<your-username>/fortune-cookie.git
git push -u origin main
```

## CI/CD pipeline

Defined in `.github/workflows/ci-cd.yml`.

1. **Trigger:** push or pull request to `main`.
2. **`test` job:** installs dependencies and runs pytest on a fresh cloud machine.
3. **`docker` job:** runs only if tests pass and only on `main`. Logs in to Docker Hub, builds the image and pushes `<username>/fortune-cookie:latest`.

Required repository secrets (Settings -> Secrets and variables -> Actions):

- `DOCKERHUB_USERNAME`: your Docker Hub username
- `DOCKERHUB_TOKEN`: a Docker Hub access token (Read & Write)

## Run the published image from anywhere

```bash
docker run -d -p 8080:5000 --name fortune <dockerhub-username>/fortune-cookie:latest
```

## How it works

```
Code -> git commit -> git push -> GitHub Actions -> Test -> Build image -> Docker Hub -> docker run anywhere
```
