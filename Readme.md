# CSCA chatbot server #
## Structure ##
### Server ###
flask + gunicorn + nginx
### Docker ###
Container with link to origin node server
## Link(Internal network) ##
### Docker Commands ###
```
docker run -d -p PORT_FLASK:PORT_FLASK -p PORT_CHATBOT_WINDOW:PORT_CHATBOT_WINDOW --link NODE_SERVER_NAME:node --name CHATBOT_SERVER_NAME chatbot:latest
```
More details in start\_docker.sh
### Python ###
#### Internal network IP ####
Obtain internal network ip of node server by
```
os.environ['NODE_PORT']
```
which will return something like tcp://172.0.0.2:5000  
  
To make http request
```
'http' + os.environ['NODE_PORT'][3:]
```
can be made.
## Notice ##
- In nginx\_conf, the server\_name must be specified.

## Instruction ##
- Build the Dockerfile
```
sudo docker build -t chatbot .
```
- Create container
```
sudo sh start_docker.sh
```
- Enter container
``` sudo docker exec -it CONTAINER_ID bash
