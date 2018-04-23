pipeline {
    agent any
    stages {
        stage ('checkout') {
            steps {
                git url: 'https://github.com/lkydig/jPython.git'
            }
        }
	stage ('show list') {
		sh 'cd /usr/bin'
		sh 'ls -al'
	}
        stage ('Unit test') {
            steps {
                sh 'python test_calculator.py'
            }
        }
    }
}
