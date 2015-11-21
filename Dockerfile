# Python-Flask Dockerfile
FROM ubuntu

MAINTAINER Herman Singh "kartstig@gmail.com"

# Fetch some repos for RabbitMQ
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
RUN apt-get update && \
  apt-get install -y curl && \
  curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -

# Install PyPy
RUN cd / && \
  curl -L -O https://bitbucket.org/pypy/pypy/downloads/pypy-2.6.1-linux64.tar.bz2 && \
  tar -xvf pypy-2.6.1-linux64.tar.bz2

# Install Pip
RUN curl -L -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py && \
  /pypy-2.6.1-linux64/bin/pypy get-pip.py

# Install Requirements
RUN apt-get update && \
  apt-get install -y \
  openssh-server \
  git \
  libzmq3 \
  libmysqlclient-dev \
  libevent-dev \
  python-dev \
  python-pip \
  libffi-dev \
  libssl-dev \
  build-essential \
  rabbitmq-server

# Application Setup
RUN mkdir /appdata
ADD . /appdata
ADD Config.py /appdata/Config.py
RUN chmod +x /appdata/run.sh

# Python Environment
RUN /pypy-2.6.1-linux64/bin/pip install virtualenv && \
  /pypy-2.6.1-linux64/bin/virtualenv --no-site-packages --distribute --python=/pypy-2.6.1-linux64/bin/pypy flask-pypy && \
  /flask-pypy/bin/pip install -r /appdata/requirements.txt

# Set up Directories
WORKDIR /appdata

# Expose Ports
EXPOSE 80

# Execute Start Script
CMD ./run.sh
