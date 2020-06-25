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
}
