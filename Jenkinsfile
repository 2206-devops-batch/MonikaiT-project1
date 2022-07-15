pipeline {
    agent any
    stages {
        stage("build") {
            steps 
                git 'https://github.com/2206-devops-batch/MonikaiT-project1.git'

                sh """
                    python3 -m venv .venv
                    pip3 install -r requirements.txt
                    python3 -m pytest app-test.py
                    docker build . -t mtinsonk/mtkproject2
                    docker login --username=mtinsonk --password=Mauria1234
                    docker push mtinsonk/mtkproject2
                    docker run -rm mtinson/mtkproject2
                """
            }
        }
    }

