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

    stage('Node Test') {
      steps {
        sh 'echo "in the node"'
      }
    }

  }
}