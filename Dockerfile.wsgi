FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "/python-docker/src/python/app_standalone.py"]