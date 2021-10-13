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
                                sh 'docker tag bitcoin:latest oday2211/bitcoin'
				sh 'docker push oday2211/bitcoin'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
