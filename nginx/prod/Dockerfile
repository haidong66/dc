FROM nginx:latest

COPY prod/nginx-prod.conf /etc/nginx/nginx.conf
COPY prod/ssl_certificate.crt /etc/nginx/certs/server.crt
COPY prod/ssl_certificate.key /etc/nginx/certs/server.key
