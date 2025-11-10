# k8s-fastapi-starter

A starter project for deploying a **FastAPI REST API** into a **local Kubernetes cluster** using **Rancher Desktop**.

This repository serves as a foundation for learning how to:
- Containerize a FastAPI application with Docker  
- Deploy it to Kubernetes using manifests (`Deployment`, `Service`, `Ingress`)  
- Scale replicas of the API horizontally  
- Automate CI/CD using GitHub Actions and GitHub Container Registry (GHCR)

---

## Architecture overview

```text
+---------------------------+
| Traefik (Ingress - Rancher Desktop) |
|  api.localhost            |
+-----------+---------------+
            |
            v
+---------------------------+
| Service (ClusterIP:80→8000)|
+-----------+---------------+
            |
            v
     +-------------+   +-------------+   +-------------+   +-------------+
     | Pod #1      |   | Pod #2      |   | Pod #3      |   | Pod #4      |
     | uvicorn app |   | uvicorn app |   | uvicorn app |   | uvicorn app |
     +-------------+   +-------------+   +-------------+   +-------------+
```
---

## Tech stack
- Component	Description
- FastAPI	Python web framework for building fast APIs
- Uvicorn	High-performance ASGI web server
- Docker	Containerization of the application
- Kubernetes (k3s)	Orchestration managed by Rancher Desktop
- Traefik	Ingress controller used by Rancher Desktop
- GitHub Actions	CI/CD automation (build, test, push)
- GitHub Container Registry (GHCR)	Container image hosting

---

## Local deployment (Rancher Desktop)

- Ensure Rancher Desktop is running
- Kubernetes must be enabled
- Traefik is preinstalled as the ingress controller
- Create the namespace
```bash
kubectl apply -f k8s/namespace.yaml
```

- Apply the manifests
```bash
kubectl -n demo apply -f k8s/deployment.yaml
kubectl -n demo apply -f k8s/service.yaml
kubectl -n demo apply -f k8s/ingress.yaml
```

- Check that pods are running
```bash
kubectl -n demo get pods
```
---
## Test the API
- Open in your browser:

http://api.localhost/healthz
---
Manual scaling

```bash
kubectl -n demo scale deploy api --replicas=4
```
Verify:
```bash
kubectl -n demo get pods
```
