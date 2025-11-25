pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub')    // Add from Jenkins credentials
        IMAGE_NAME = "sahilakolte/calculator-app"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/sahilakolte/calculator-app'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
                sh "docker images"
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh "echo ${DOCKERHUB_PSW} | docker login -u ${DOCKERHUB_USR} --password-stdin"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }
    }
}
