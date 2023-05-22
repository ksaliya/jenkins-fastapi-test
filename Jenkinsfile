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
        sh 'docker stop api-container'
        sh 'docker rm api-container'
      }
    }
    
    stage('Deploy API') {
      steps {
        sh 'docker run -d --name api-container -p 8081:80 my-api:0.0.my-api:0.0.${BUILD_ID}'
      }
    }

  }
}
