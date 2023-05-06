FROM python:3.10.0-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

RUN apt-get install -y gcc vim curl

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata

WORKDIR /opt/projects/Centribal/

COPY . .

RUN pip --no-cache-dir install poetry

RUN poetry install

# RUN poetry run python3 manage.py makemigrations

# RUN poetry run python3 manage.py migrate