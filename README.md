# Bootcamp SRE Capstone Project

This is the capstone project for Wizeline's SRE Bootcamp.

The chosen programming language is **Python** so the node folder in parent repository has been deleted. In addition, I've renamed python folder so it makes more sense for the project file structure.

The application has been dockefized and uploaded to dockerhub: __gdanielcast/academy-sre-bootcamp-gerardo-castellanos:latest__

This image has been setup to use the database provided for testing in the project instructions **[here](https://classroom.google.com/w/MzgwNTc4MDgwMjAw/t/all)**.

## Run from docker image

Run the image with below command:

    docker run -p 8000:8000 gdanielcast/academy-sre-bootcamp-gerardo-castellanos:latest

> Note: The local host port used in the example can be changed for any other available local port.

## Build image locally

This repository includes the Dockerfile to build the image locally. In order to build the image, environmennt variables have to be defined.

The required variables are:

### Flask startup settings

- __API_HOST__
- __API_PORT__

### Database information:

- __DB_HOST__
- __DB_USER__
- __DB_PASSWORD__
- __DB_NAME__

### Secret key to sign generated tokens

- __SIGNATURE__

This environment variables can either be passed in a .env file inside the app folder or during the image build.

> .env file example:

    API_HOST='0.0.0.0'
    API_PORT=8000

    DB_HOST=******
    DB_USER******
    DB_PASSWORD=******
    DB_NAME=******

    SIGNATURE=******
