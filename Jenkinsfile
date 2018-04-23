pipeline {
    agent any
    stages {
        stage ('checkout') {
            steps {
                git url: 'https://github.com/lkydig/jPython.git'
            }
        }
	stage ('show list') {
            steps {
                sh 'apt-get install python'
                sh 'ls -al /usr/bin'
            }
	}
        stage ('Unit test') {
            steps {
                sh 'python test_calculator.py'
            }
        }
    }
}
