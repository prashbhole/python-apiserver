node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("pgbhole/python-apiserver")
    }

    stage('Test image') {
        app.inside {
            sh 'python -m unittest discover tests/unit/'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'pgbhole-docker-hub-cred') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }

    stage('Deploy image') {
        sshagent (credentials: ['ec2-18-188-226-162.us-east-2']) {

            sh """ssh -tt ubuntu@ec2-18-188-226-162.us-east-2.compute.amazonaws.com << EOF
                 docker stop python-apiserver || true && docker rm python-apiserver || true
                 docker pull pgbhole/python-apiserver
                 docker run --name python-apiserver --rm -d -p 5000:5000 pgbhole/python-apiserver
                 #TODO: Wait for container to run and the check status
                 exit
                 """
        }
    }
}
