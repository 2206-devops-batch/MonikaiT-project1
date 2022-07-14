pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                sh """
                    python3 -m venv .venv
                    pip3 install -r requirements.txt
                    python3 -m pytest app-test.py
                    docker build -t mtkproject2 .
                    docker push mtkproject2
                """
                sh 'git https://github.com/2206-devops-batch/MonikaiT-project1.git'
            }
        }
    }
}
