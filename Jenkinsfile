pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dckr_pat_MMJMtPXvlTVfTHSMnXrRoqZILOk')
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

        stage('CreateVolume') {
            steps {
                script {
                    docker volume create world_of_games
                }
            }
        }


    }
}