pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dckr_pat_MMJMtPXvlTVfTHSMnXrRoqZILOk')
        DOCKER_IMAGE = 'rtyuiioo/wog:1.12'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([ branch: 'main', url: 'https://github.com/Yasha12345656786/Wog.git' ])
            }
        }
    }

    }
}