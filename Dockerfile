FROM python:3.9-slim AS base

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get clean

FROM base AS app

COPY . /usr/test_project

WORKDIR /usr/test_project

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]