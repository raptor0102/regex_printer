FROM python:3.7

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project/
RUN pip install --no-cache-dir -r requirements.txt


COPY tests /project/tests
COPY src /project/src
