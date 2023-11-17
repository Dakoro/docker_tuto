LABEL org.opencontainers.image.source="https://github.com/Dakoro/docker_tuto"

FROM python:3-alpine

WORKDIR /app_python

COPY hello.py hello.py
COPY requirements.txt requirements.txt

ARG NAME

ENV NAME=${NAME}

RUN python3 -m venv /app_python/env
RUN . /app_python/env/bin/activate && pip install -r requirements.txt

CMD . /app_python/env/bin/activate && exec python /app_python/hello.py

