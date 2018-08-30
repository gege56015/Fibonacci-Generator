## Simple RESTful API For Generating a Fibonacci Sequence

This repo contains a simple service written in Python using the Flask framework as well as Pytest for unit testing. Once the service is running, simply give it a number, and it will generate a fibonacci sequence ending at that number. 

This service was the result of a brief coding exercise intended to demonstrate a Flask API. As such, extended effort was NOT put into this project. There is more that could be done to make this service more robust (e.g. paging etc).

<p>&nbsp;</p>

## How To Use:

[On Localhost With Docker And Docker Compose](#localhost-with-docker-and-docker-compose)

[On Localhost Without Docker](#localhost-without-docker)


<p>&nbsp;</p>

**On Localhost With Docker and Docker Compose** <a id="localhost-with-docker-and-docker-compose"></a>

This is the simplest method of bringing up the service, as it is automatically handled by Docker Compose. It does not require you to use a cloud account nor a server, you can simply use your local machine. 

1. Clone this repository to a local directory
2. From the project's root directory, type "docker-compose up -d"
3. In your web browser, visit http://localhost:8000 for simple instructions on how to use the service

<p>&nbsp;</p>

**On Localhost Without Docker** <a id="localhost-without-docker"></a>

This method bypasses the Docker containerization approach and allows you to run the service directly (using a Pipenv-managed virtual environment). Note that this method does not use Nginx in front of gunicorn.

1. Clone this repository to a local directory
2. Make sure you have pipenv installed. If not, you can type 'pip install pipenv' to install it.
3. To **_scan all dependencies for known security vulnerabilities_**, type "pipenv check" from the project's "app" directory
4. To **_run unit tests_**, type "pipenv run pytest" from the project's "app" directory
5. To run the service, type "pipenv run gunicorn wsgi" from the project's "app/main" directory
6. In your web browser, visit http://localhost:8000 for simple instructions on how to use the service




