pipeline {
    agent any

    environment {
        IMAGE = "sahilakolte/calculator-app:latest"
        VENV = ".venv"
        PYTHON = "/usr/bin/python3" 
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[
                    url: 'https://github.com/sahilakolte/calculator-app.git',
                    credentialsId: 'github'
                  ]]
                ])
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '$PYTHON -m venv $VENV'
                sh '$VENV/bin/pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '$VENV/bin/pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                          usernameVariable: 'USER',
                                          passwordVariable: 'PASS')]) {
            sh '''
              echo $PASS | docker login -u $USER --password-stdin
              docker build -t $IMAGE .
              docker logout
            '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh '''
                      echo $PASS | docker login -u $USER --password-stdin
                      docker push $IMAGE
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                  docker pull $IMAGE
                  docker stop calculator-app || true
                  docker rm calculator-app || true
                  docker run -d -p 5000:5000 --name calculator-app $IMAGE
                '''
            }
        }
    }
}