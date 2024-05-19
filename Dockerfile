FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV GIT_PYTHON_REFRESH=warning
	
RUN apk update
RUN apk add mysql-dev
RUN apk add postgresql-dev
RUN apk add libc-dev
RUN apk add linux-headers
RUN apk add gcc
RUN apk add libffi-dev
RUN apk add --no-cache  
RUN apk add git
RUN apk add --no-cache libaio
RUN apk add --no-cache curl
RUN apk add --no-cache musl
RUN apk add --no-cache gcompat
RUN apk add --no-cache python3-dev
RUN apk add --no-cache libnsl-dev
RUN apk add --no-cache build-base
RUN apk add poetry

# Download and install Oracle Instant Client
RUN curl -o instantclient-basiclite.zip https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip -SL && \
    unzip instantclient-basiclite.zip && \
    mv instantclient*/ /usr/lib/instantclient && \
    rm instantclient-basiclite.zip && \
    ln -s /usr/lib/instantclient/libclntsh.so.19.1 /libclntsh.so && \
    ln -s /usr/lib/instantclient/libocci.so.19.1 /libocci.so && \
    ln -s /usr/lib/instantclient/libociicus.so /libociicus.so && \
    ln -s /usr/lib/instantclient/libnnz19.so /libnnz19.so && \
    ln -s /usr/lib/libnsl.so.2 /libnsl.so.1 && \
    ln -s /lib/libc.so.6 /libresolv.so.2 && \
    ln -s /lib64/ld-linux-x86-64.so.2 /ld-linux-x86-64.so.2

ENV ORACLE_BASE /usr/lib/instantclient
ENV LD_LIBRARY_PATH /usr/lib/instantclient
ENV TNS_ADMIN /usr/lib/instantclient
ENV ORACLE_HOME /usr/lib/instantclient

# Install JAVA for allure
RUN apk add --no-cache openjdk11-jre
RUN apk upgrade

ENV JAVA_HOME /usr/lib/jvm/default-jvm

RUN curl -o allure-2.26.0.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.26.0/allure-commandline-2.26.0.tgz && \
    tar -zxvf allure-2.26.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.26.0/bin/allure /usr/bin/allure && \
    rm allure-2.26.0.tgz



# Install all python library requirements
COPY . /home
WORKDIR /home

# RUN poetry add 'Cython<3.0.0'
RUN poetry add PyYAML oracledb==1.2.2

RUN poetry install 

RUN chmod +x /home/startup.sh
ENTRYPOINT /home/startup.sh