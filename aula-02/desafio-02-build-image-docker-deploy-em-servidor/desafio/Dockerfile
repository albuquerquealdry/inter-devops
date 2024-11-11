FROM nginx:latest
RUN rm /usr/share/nginx/html/index.html
RUN pwd 
COPY outro_repo/index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]