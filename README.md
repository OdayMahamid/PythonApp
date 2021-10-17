# PythonApp

## Instructions for running the app via Dockerfile
#build docker image

docker build -t bitcoin .

#run docker image

docker run -it -p:5000:8888 bitcoin

#run the following url on brwoser to see the application running: http://127.0.0.1:5000/BitcoinPrice

![WhatsApp Image 2021-10-14 at 14 01 57](https://user-images.githubusercontent.com/58177069/137306813-1011ceee-69ca-4690-88b7-8f3dda1db3cd.jpeg)

### The purpose of Jenkinsfile is to push the image to dokcerhub,for that I add a credential from dockerhub to jenkins in order to login in dockerhub by jenkins

### we see the pipeline is success and add the docker image to dockerhub.

### Note: I build this image in jenkins server in order to push it.

![Wha](https://user-images.githubusercontent.com/58177069/137307626-4de834c6-0ff6-4de9-a024-3fc427b898fc.jpeg)
![hub](https://user-images.githubusercontent.com/58177069/137307643-a74159c9-36e1-44d8-bcc0-f45d6c9a1ef7.jpeg)
