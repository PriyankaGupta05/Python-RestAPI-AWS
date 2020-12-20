# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY . /usr/src/app

# Install API dependencies
RUN pipenv install
RUN pip install -r requirements.txt

# Start app
EXPOSE 9880
ENTRYPOINT ["/usr/src/app/run.sh"]
