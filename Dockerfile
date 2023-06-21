FROM mysql:latest
MAINTAINER krishnakumar
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=user_db
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
COPY init.sql /docker-entrypoint-initdb.d/

