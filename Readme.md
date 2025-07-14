
1. Project CloudLaunch
- A Python Flask App with Docker, Kubernetes & GitHub Actions CI/CD

## Project Structure
my-cloud-project/
├── app/
│ ├── app.py
│ └── requirements.txt
├── Dockerfile
├── .dockerignore
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
├── .github/
│ └── workflows/
│ └── ci-cd.yml
├── README.md


2. 🧠 Description
This project demonstrates how to containerize a simple Python Flask app using Docker, deploy it on Kubernetes, and automate the build & deployment process with GitHub Actions CI/CD pipeline.


3. 🎯 Project Objectives.

To learn:
- Containerizing the app with Docker 🐳 — I wrote my own Dockerfile to package the app efficiently.

- Defining Kubernetes infrastructure by hand 📄 — I created custom deployment and service YAML files following official docs, giving me deep insight into container orchestration.

- Deploying on Amazon EKS ☁️🚀 — I took the app to the cloud, managing cluster creation and scaling with Kubernetes.

- Implementing security best practices 🔐 — I managed sensitive tokens via GitHub repository secrets to keep credentials safe.

- Building a custom CI/CD pipeline with GitHub Actions 🤖 — From code commit to deployment, I automated the entire workflow, ensuring seamless updates.

- Learning and adapting every step of the way 📚✨ — This project was a crash course in DevOps, cloud, and infrastructure as code.


4. 🛠️ Technical Overview
- Flask app -  that returns a simple "Hello, World!" response.
- Dockerized application -  using a custom Dockerfile.
- Kubernetes deployment - using YAML files for Deployment & Service.
- CI/CD pipeline - using GitHub Actions to automate builds and deployments.
- Secrets managed securely -  through GitHub Secrets.
- Optional local deployment with Docker or a Kubernetes cluster (e.g., Minikube).

5. 🚀 Getting Started
Create the following secrets in your repository under
Settings → Secrets and variables → Actions:

DOCKER_USERNAME — Your Docker Hub username

DOCKER_PASSWORD — Your Docker Hub password or access token

KUBE_CONFIG_DATA — Base64-encoded Kubernetes config file

Push your code to GitHub to trigger the pipeline:

git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/sunsembrace/Project-CloudLaunch.git
git branch -M main
git push -u origin main


6. 🧪 Usage
CI/CD is triggered automatically on push to the main branch.

The pipeline:

Builds the Docker image.

Pushes it to Docker Hub.

Deploys to your Kubernetes cluster using kubectl.


7. 🔧 Configuration
Make sure your Kubernetes config (~/.kube/config) is base64 encoded before storing as a secret:


base64 ~/.kube/config
Paste the output into the GitHub secret named KUBE_CONFIG_DATA.


8. 💻 Tech Stack
- Python + Flask 🐍

- Docker 🐳

- Kubernetes ☸️

- Amazon EKS or local clusters (Minikube/Docker Desktop)

- GitHub Actions 🤖


9. Architecture flow
A[GitHub Commit] --> B[GitHub Actions CI/CD]
B --> C[Docker Build]
C --> D[Push to Docker Hub]
D --> E[Kubectl Deploy]
E --> F[Kubernetes Cluster (EKS/Minikube)]
F --> G[Running Flask App]


10. 🐞 Known Limitations
LoadBalancer services require a cloud provider (e.g., AWS EKS). For local testing, you may need to use NodePort or port forwarding.

The app is intentionally minimal—no advanced Flask features.


11. ✍️ Future Improvements
- Add Helm charts for more scalable deployments.

- Implement rollback strategies in the CI/CD pipeline.

- Add monitoring via Prometheus + Grafana.

- Add environment-specific configurations (dev/staging/prod).

- Add unit testing and linting steps to the pipeline.


12. 📄 License
This project is licensed under the MIT License.


13. 🙏 Acknowledgements
- Kubernetes Docs

- Docker Docs

- GitHub Actions Docs

- AWS EKS Guide


14. 💡 Challenges & Solutions
Challenge: Managing secrets securely for CI/CD.
Solution: Used GitHub Secrets to prevent exposure of sensitive credentials.

Challenge: Understanding Kubernetes YAML structure.
Solution: Referred to official documentation and broke down each manifest piece-by-piece.

Challenge: Automating deployment to EKS.
Solution: Encoded kubeconfig securely and used GitHub Actions with kubectl.


