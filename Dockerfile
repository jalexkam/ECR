FROM nginx:latest
RUN touch /usr/share/nginx/html/index.html
RUN CHMOD 777 /usr/share/nginx/html/index.html
EXPOSE 80

# Create the index.html file within the Dockerfile
RUN echo "<html><head><title>My Website</title></head><body><h1>Hello from my Dockerized Nginx server!</h1></body></html>" > /usr/share/nginx/html/index.html
