# 🚀 AWS Containerized CI/CD Pipeline using GitHub, Docker, Amazon ECR & Amazon ECS Fargate

## 📌 Project Overview

This project demonstrates a **production-style Continuous Integration and Continuous Deployment (CI/CD) pipeline** built entirely on **Amazon Web Services (AWS)** for a **Dockerized Flask web application**.

The pipeline automatically detects every code change pushed to the GitHub repository, builds a Docker image, executes automated tests, pushes the image to **Amazon Elastic Container Registry (ECR)**, and deploys the latest version to **Amazon ECS Fargate** without requiring any manual intervention.

The application is served through an **Application Load Balancer (ALB)**, allowing users to access the latest deployed version through a single public endpoint while maintaining high availability and scalability.

This project demonstrates modern **Cloud DevOps practices**, containerization, Infrastructure as a Service (IaaS), Platform as a Service (PaaS), automated software delivery, and cloud-native application deployment using AWS Developer Tools.

---

# 🎯 Project Objectives

* Build a fully automated CI/CD pipeline on AWS
* Containerize a Flask application using Docker
* Store Docker images securely in Amazon ECR
* Automatically deploy new application versions using Amazon ECS Fargate
* Eliminate manual deployment processes
* Demonstrate cloud-native deployment practices
* Implement scalable container orchestration
* Integrate GitHub with AWS Developer Tools
* Showcase DevOps automation suitable for production environments

---

# 🏗️ Project Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     │ Push Code
     ▼
AWS CodePipeline
     │
     ▼
AWS CodeBuild
     │
     ├── Install Dependencies
     ├── Run Tests
     ├── Build Docker Image
     ├── Login to Amazon ECR
     ├── Push Docker Image
     └── Generate imagedefinitions.json
               │
               ▼
Amazon Elastic Container Registry (ECR)
               │
               ▼
Amazon ECS Fargate
               │
               ▼
ECS Service
               │
               ▼
Running ECS Tasks
               │
               ▼
Application Load Balancer
               │
               ▼
Users Access Application
               │
               ▼
CloudWatch Logs & Monitoring
```

---

# 🛠 AWS Services Used

| Service                                 | Purpose                 |
| --------------------------------------- | ----------------------- |
| GitHub                                  | Source code repository  |
| AWS CodePipeline                        | CI/CD orchestration     |
| AWS CodeBuild                           | Build automation        |
| Amazon Elastic Container Registry (ECR) | Docker image storage    |
| Amazon ECS Fargate                      | Container orchestration |
| Application Load Balancer               | Traffic distribution    |
| ECS Cluster                             | Container hosting       |
| ECS Service                             | Service management      |
| ECS Task Definition                     | Container configuration |
| ECS Tasks                               | Running containers      |
| Amazon CloudWatch                       | Logging and monitoring  |
| IAM                                     | Roles and permissions   |
| Docker                                  | Containerization        |

---

# 📂 Project Workflow

## Step 1 — Application Development

A Flask web application was developed with:

* Responsive landing page
* Project information
* Health endpoint (`/health`)
* Production status page
* Environment information
* Version details

---

## Step 2 — Docker Containerization

The application was containerized using Docker.

The Dockerfile performs:

* Pull Python base image
* Install dependencies
* Copy application
* Expose port 5000
* Start Flask application

Benefits:

* Consistent runtime
* Portable deployment
* Immutable infrastructure

---

## Step 3 — Source Code Management

The complete project was pushed to GitHub.

Repository includes:

```
templates/
tests/
app.py
Dockerfile
requirements.txt
buildspec.yml
README.md
.gitignore
```

GitHub acts as the pipeline trigger.

---

## Step 4 — Continuous Integration using AWS CodePipeline

AWS CodePipeline continuously monitors the GitHub repository.

Whenever code is pushed:

1. Detects commit
2. Downloads source
3. Starts CodeBuild
4. Waits for build completion
5. Triggers deployment
6. Deploys latest version automatically

No manual deployment is required.

---

## Step 5 — Automated Build using AWS CodeBuild

AWS CodeBuild performs:

### Install Phase

* Install Python
* Install project dependencies
* Install testing packages

### Pre-Build Phase

* Execute automated tests
* Retrieve AWS Account ID
* Retrieve AWS Region
* Authenticate with Amazon ECR

### Build Phase

* Build Docker image
* Tag Docker image
* Prepare deployment artifact

### Post-Build Phase

* Push Docker image to Amazon ECR
* Generate `imagedefinitions.json`
* Upload artifacts to CodePipeline

---

# Sample buildspec.yml Workflow

```
Install Dependencies

↓

Run Tests

↓

Authenticate with Amazon ECR

↓

Build Docker Image

↓

Tag Image

↓

Push Image to ECR

↓

Generate imagedefinitions.json

↓

Upload Artifact
```

---

# Step 6 — Amazon Elastic Container Registry (ECR)

Amazon ECR serves as the Docker image repository.

Responsibilities:

* Store versioned Docker images
* Secure image storage
* Integrate with ECS
* Maintain image history

Each successful build pushes:

```
latest

commit-id tag
```

---

# Step 7 — Amazon ECS Fargate

Amazon ECS Fargate removes the need to manage EC2 instances.

Responsibilities:

* Pull image from ECR
* Launch container
* Monitor task health
* Restart failed containers automatically
* Scale containers

Benefits:

* Serverless containers
* No infrastructure management
* Automatic resource allocation

---

# Step 8 — ECS Task Definition

Defines:

* Docker image
* CPU
* Memory
* Port mappings
* Logging
* Container name
* Environment variables

Acts as the deployment blueprint.

---

# Step 9 — ECS Service

The ECS Service ensures:

* Desired number of running tasks
* Automatic replacement of failed tasks
* Rolling deployments
* Load balancer integration

---

# Step 10 — Application Load Balancer

The ALB distributes traffic across ECS tasks.

Responsibilities:

* Public endpoint
* Health checks
* Target registration
* Traffic routing
* Zero-downtime deployments

Health check endpoint:

```
/health
```

---

# Step 11 — Target Group

Target Group continuously checks:

```
HTTP GET /health
```

If healthy:

```
Healthy
```

Otherwise:

```
Unhealthy
```

Only healthy containers receive traffic.

---

# Step 12 — CloudWatch Logs

CloudWatch collects:

* Container logs
* Application logs
* Build logs
* ECS deployment logs

Useful for:

* Monitoring
* Troubleshooting
* Auditing

---

# Step 13 — Continuous Deployment

Every GitHub push automatically performs:

```
Developer Pushes Code

↓

GitHub

↓

CodePipeline Trigger

↓

CodeBuild

↓

Docker Build

↓

Push Image to ECR

↓

Deploy ECS

↓

Replace Running Tasks

↓

ALB Serves Latest Version
```

Entire deployment is automatic.

---

# 📁 Repository Structure

```
aws-docker-cicd-webapp
│
├── templates
│   └── index.html
│
├── tests
│   └── test_app.py
│
├── Dockerfile
├── buildspec.yml
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── architecture-diagram.png
```

---

# ✨ Features

* Fully automated CI/CD pipeline
* Docker containerization
* GitHub integration
* Continuous Integration
* Continuous Deployment
* Automated testing
* Container image versioning
* Amazon ECR integration
* Amazon ECS Fargate deployment
* Application Load Balancer
* CloudWatch logging
* Health monitoring endpoint
* Zero manual deployments
* Rolling deployments
* Production-style architecture

---

# 🚀 Deployment Workflow

```
Developer

↓

Git Push

↓

GitHub Repository

↓

AWS CodePipeline

↓

AWS CodeBuild

↓

Run Tests

↓

Docker Build

↓

Push Image

↓

Amazon ECR

↓

Amazon ECS Service

↓

Running ECS Tasks

↓

Application Load Balancer

↓

Application Available to Users
```

---

# 📊 Skills Demonstrated

* AWS Cloud
* DevOps
* Continuous Integration
* Continuous Deployment
* Docker
* Containerization
* Amazon ECS
* Amazon ECR
* AWS CodePipeline
* AWS CodeBuild
* Application Load Balancer
* CloudWatch
* IAM
* Git
* GitHub
* Flask
* Python
* Linux
* Cloud Automation
* Infrastructure Automation

---

# 📸 Suggested Repository Screenshots

Include the following screenshots in your GitHub repository for better presentation:

1. Architecture Diagram
2. GitHub Repository
3. Dockerfile
4. buildspec.yml
5. AWS CodePipeline (Source → Build → Deploy)
6. Successful CodeBuild Execution
7. Amazon ECR Repository with Image Tags
8. ECS Cluster
9. ECS Service
10. ECS Running Task
11. ECS Task Definition
12. Application Load Balancer
13. Target Group (Healthy Targets)
14. CloudWatch Logs
15. Running Web Application
16. `/health` Endpoint Response
17. ECS Deployment History
18. ECS Service Events

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Designing and implementing production-style CI/CD pipelines
* Containerizing Python applications using Docker
* Automating software delivery with AWS Developer Tools
* Managing container images in Amazon ECR
* Deploying containerized applications on Amazon ECS Fargate
* Configuring Application Load Balancers and health checks
* Monitoring applications with Amazon CloudWatch
* Integrating GitHub with AWS for continuous deployment
* Implementing cloud-native deployment strategies following DevOps best practices

---

## 🏁 Conclusion

This project demonstrates a complete end-to-end cloud-native CI/CD workflow on AWS, beginning with a GitHub code commit and ending with an automatically deployed, highly available application running on Amazon ECS Fargate behind an Application Load Balancer. By combining GitHub, AWS CodePipeline, CodeBuild, Amazon ECR, ECS Fargate, CloudWatch, IAM, and Docker, it showcases modern DevOps automation practices that reduce manual effort, improve deployment reliability, and accelerate software delivery. The architecture reflects production-oriented principles such as containerization, automated testing, rolling deployments, health monitoring, and continuous delivery, making it a strong portfolio project for Cloud, DevOps, and Platform Engineering roles.
