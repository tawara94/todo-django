FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
