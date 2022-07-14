pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                sh """
                    python3 -m venv .venv
                    . .venv/Scripts/activate
                    pip install -r requirements-dev.txt
                    python3 -m pytest app-test.py
                    docker build -t mtk_project2 .
                    docker push mtk_project2
                """
                sh 'git https://github.com/2206-devops-batch/MonikaiT-project1.git'
            }
        }
        stage("run") {
            steps{
                sh """
                    docker run --rm mtk_project2
                """
            }
        }
    }
}
