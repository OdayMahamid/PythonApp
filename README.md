# PythonApp

## Instructions for running the app via DOCKERfile
#build docker image

docker build -t bitcoin .

#run docker image

docker run -it -p:5000:5000 bitcoin

#run the following url on brwoser to see the application running: http://127.0.0.1:5000/BitcoinPrice

