pipeline {
  agent {
    node {
      label 'andromeda'
    }

  }
  stages {
    stage('pull from git') {
      steps {
        git(url: 'https://github.com/ksaliya/jenkins-fastapi-test.git', branch: 'master')
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t my-api:0.0.${BUILD_ID} .'
      }
    }

    stage('Remove Old Container') {
      steps {
        sh '''if docker ps -a --format \'{{.Names}}\' | grep -q \'api-container\'; then
  docker stop api-container
  docker rm api-container
fi'''
      }
    }

    stage('Deploy API') {
      steps {
        sh 'docker run -d --name api-container -p 8081:80 my-api:0.0.${BUILD_ID}'
      }
    }

  }
}