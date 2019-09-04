docker run -d -p 5000:5000 -p 80:80 --link node_server:host --name chatbot_server chatbot:latest
