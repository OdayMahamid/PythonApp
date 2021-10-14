# PythonApp

## Instructions for running the app via DOCKERfile
#build docker image

docker build -t bitcoin .

#run docker image

docker run -it -p:5000:5000 bitcoin

#run the following url on brwoser to see the application running: http://127.0.0.1:5000/BitcoinPrice

![WhatsApp Image 2021-10-14 at 14 01 57](https://user-images.githubusercontent.com/58177069/137306813-1011ceee-69ca-4690-88b7-8f3dda1db3cd.jpeg)

the purpose of Jenkinsfile is to push the image to dokcerhub,I add a credential 
