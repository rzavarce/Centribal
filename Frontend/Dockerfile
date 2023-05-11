# Build stage
FROM node:latest

# RUN apk --update

RUN mkdir -p /opt/projects/Centribal/

WORKDIR /opt/projects/Centribal/

COPY ./Frontend /opt/projects/Centribal/

RUN npm install

RUN npm install -g @quasar/cli

RUN quasar build

# Runtime stage
FROM nginx
ENV projectName "CentribalTest"
COPY ./Frontend/dist/spa/. /usr/share/nginx/html
COPY ./Frontend/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080


