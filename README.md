# github-actions-python
GitHub Actions workflow for s simple Python project to print Hello World.

This repository contains a GitHub Actions workflow for building a Python project, creating a Python package, building and pushing a Docker image, and scanning it using Trivy. 

#### Workflow Description

The workflow consists of two main jobs:

helloworld-build: Builds the Python project, runs tests, creates a Python package, deploys it, and archives artifacts.
docker-build: Builds a Docker image using the Python package from the previous job, pushes it to Docker Hub, scans it for vulnerabilities using Trivy, and runs a container to validate functionality.

#### Job Breakdown

**Job: helloworld-build**
Steps:

1. Checkout code: Retrieves the source code from the repository.
2. Set up Python 3.7: Configures the environment with Python version 3.7. 
3. Install dependencies: Installs project dependencies and prepares for testing. 
4. Run Unit Tests and generate coverage report: Executes unit tests, generates coverage reports using coverage, and publishes HTML reports. 
5. Archive code coverage HTML report: Archives the HTML coverage report as an artifact. 
6. Run package creation: Installs build package builder and creates a Python package. 
7. Deploy Python Package: Runs the Python script src/helloworld/core.py after package creation. 
8. Archive package: Archives the Python package as an artifact.

**Job: docker-build**
Dependencies:

Depends on artifacts produced by helloworld-build job.
Steps:

1. Checkout code: Retrieves the source code from the repository. 
2. Download artifacts: Downloads artifacts (Python package) produced by helloworld-build job. 
3. Build Docker image: Builds a Docker image named lipikapal/lptest-hello-world using the Python package. 
4. Push Docker image: Authenticates with Docker Hub using secrets, pushes the Docker image to the repository. 
5. Install Trivy: Installs Trivy, a vulnerability scanner for containers. 
6. Scan Docker image with Trivy: Scans the pushed Docker image for vulnerabilities using Trivy. 
7. Run Docker container and print output: Runs a Docker container from the pushed image and verifies its functionality.
