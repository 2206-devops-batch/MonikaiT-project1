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
                    kill -9 12749
                    docker run --name=jenkins-master -p 8080:8080 -p 50000:50000 -v /var/jenkins_home -d jenkins/jenkins
                """
            }
        }
    }
}

