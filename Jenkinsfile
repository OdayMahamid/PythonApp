pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('DockerHub')
	}

	stages {

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
                                sh 'docker tag bitcoin oday2211/bitcoin-usd'
				sh 'docker push oday2211/bitcoin-usd'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
