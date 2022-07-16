pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                sh """
                    python3 -m venv .venv
                    pip3 install -r requirements.txt
                    python3 -m pytest app-test.py
                    docker image prune -af
                    docker system prune -af
                    docker container prune -f
                    docker build . -t mtinsonk/mtkproject2
                    docker build . -t mtinsonk/server-mtkproject2
                    docker build . -t mtinsonk/jenkins-mtkproject2
                    docker login --username=mtinsonk --password=Mauria1234
                    docker push mtinsonk/mtkproject2
                    docker push mtinsonk/server-mtkproject2
                    docker push mtinsonk/jenkins-mtkproject2
                """
            }
        }
    }
}


