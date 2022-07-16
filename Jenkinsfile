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
                    #docker stop \$(docker ps -qa)
                    #docker rm -fv \$(docker ps -qa)
                    docker container prune -f
                    docker build . -t mtinsonk/mtkproject2
                    docker login --username=mtinsonk --password=Mauria1234
                    docker push mtinsonk/mtkproject2
                """
            }
        }
        stage("run") {
            steps {
                sh """
                    docker run --rm -d mtinsonk/mtkproject2
                    docker pull jenkins/jenkins
                    docker run -p 8082:8080 --name=jenkins-master -d jenkins/jenkins
                    #minikube start
                """
            }
        }
    }
}

