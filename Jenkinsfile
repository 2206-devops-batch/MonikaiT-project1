pipeline {
     environment { 
        registry = "mtinsonk/mtkproject2"
        registtryCredential = 'mtinsonk'
        dockerImage = 'mtinsonk/mtkproject2' 
    }
    agent any
    stages {
        stage('Cloning our Git') { 
            steps { 
                git 'https://github.com/2206-devops-batch/MonikaiT-project1.git'
            }
        }
        stage("build") {
            steps {
                sh """
                    python3 -m venv .venv
                    pip3 install -r requirements.txt
                    python3 -m pytest app-test.py
                    docker image prune -af
                    docker system prune -af
                    docker container prune -f
                    docker build . -t mtinsonk/mtkproject2:latest
                    docker build . -t mtinsonk/server-mtkproject2
                    docker build . -t mtinsonk/jenkins-mtkproject2
                    docker push mtinsonk/mtkproject2
                    docker push mtinsonk/server-mtkproject2
                    docker push mtinsonk/jenkins-mtkproject2
                    docker run -d -p 8000:8000 mtinsonk/mtkproject2:latest
                """
            }
        }
    }
     post {
        // Clean after build
        always {
            cleanWs(cleanWhenNotBuilt: true,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true,
                    patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                               [pattern: '.propsfile', type: 'EXCLUDE']])
        }
    }
}
//