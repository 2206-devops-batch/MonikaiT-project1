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
                """
            }
        }
        stage("cluster") {
            agent {label 'linux'}
            steps {
                sh """
                    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
                    install minikube-linux-amd64 /usr/local/bin/minikube
                    snap install kubectl --classic
                    kubectl version --client
                    minikube start
                    minikube status
                    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
                    chmod 700 get_helm.sh
                    ./get_helm.sh
                """
            }
        }
    }
}

