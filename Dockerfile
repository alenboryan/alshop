# Base image
FROM ubuntu:18.04

# Set environment variables for non-interactive installations
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

# Install system dependencies
RUN apt-get clean && apt-get update && apt-get install -y \
    locales \
    python3 python3-pip python3-dev \
    libpq-dev gcc postgresql-client postgresql-server-dev-all \
    curl zip unzip apt-utils && \
    locale-gen en_US.UTF-8 && \
    apt-get -y upgrade && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Copy the requirements file and install Python dependencies
COPY requirements.txt /data/requirements.txt
RUN pip3 install -r /data/requirements.txt

# Set the working directory
WORKDIR /data

# Copy the application code
COPY . /data/

# Run the application
CMD ["bash", "-c", "python3 ./alshop/manage.py makemigrations && python3 ./alshop/manage.py migrate && python3 ./alshop/manage.py runserver 0.0.0.0:8000"]