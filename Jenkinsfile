pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('')
        DOCKER_IMAGE = 'rtyuiioo/wog:1.12'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Yasha12345656786/Wog.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run('-p 8777:5000 -v $PWD/Scores.txt:/Scores.txt --name flaskapp')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python e2e.py'
                    } catch (Exception e) {
                        error("Tests failed")
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop flaskapp'
                    sh 'docker rm flaskapp'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'DOCKERHUB_CREDENTIALS') {
                        docker.image(DOCKER_IMAGE).push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}