FROM python:3.9-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt
COPY . /app
