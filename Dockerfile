FROM python:3.9-slim AS base

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get install make -y \
    && apt-get clean

FROM base AS app

WORKDIR /usr/test_project

COPY requirements.txt /usr/test_project/
RUN pip install -r requirements.txt

COPY .env alembic.ini entrypoint-server.sh /usr/test_project/

COPY src /usr/test_project