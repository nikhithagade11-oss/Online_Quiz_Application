
pipeline {
    agent any

    environment {
        IMAGE_NAME = "online-quiz"
        DOCKER = "C:\\Users\\User\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe"
        KUBECTL = "C:\\Users\\User\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\kubectl.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '"%KUBECTL%" apply -f deployment.yaml'
                bat '"%KUBECTL%" set image deployment/online-quiz-deployment online-quiz=%IMAGE_NAME%:%BUILD_NUMBER%'
                bat '"%KUBECTL%" rollout status deployment/online-quiz-deployment'
            }
        }
    }
}
