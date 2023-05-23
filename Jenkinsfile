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
        sh 'docker compose up -d --build'
      }
    }
  }
}