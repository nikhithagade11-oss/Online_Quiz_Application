
pipeline {
    agent any

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
                bat '"C:\\Users\\User\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t online-quiz:latest .'
                }
            }
        }
    }
}
