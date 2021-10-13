pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('DockerHub')
	}

	stages {

		stage('Build') {

			steps {
                               sh 'sudo chmod 666 /var/run/docker.sock'
                               echo 2211
				sh 'docker build -t bitcoin .'

			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push oday2211/bitcoin:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
