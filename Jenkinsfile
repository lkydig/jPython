pipeline {
    agent any
    stages {
        stage ('checkout') {
            steps {
                git url: 'https://github.com/lkydig/jPython.git'
            }
        }
        stage ('Unit test') {
            steps {
                sh '/usr/bin/python test_calculator.py'
            }
        }
    }
}
