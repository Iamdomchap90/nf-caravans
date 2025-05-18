FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off

WORKDIR /app

ENV \
  PATH="/root/.local/bin:$PATH"

RUN set -ex \
  && apt-get update && apt-get -y --no-install-recommends install make \
  && pip install poetry==1.6.1 \
  && poetry config virtualenvs.create false

COPY pyproject.toml /app/

RUN set -ex \
  && poetry install $(test "$BUILD_ENV" = production && echo "--no-dev") --no-root --no-interaction --no-ansi

FROM base as full

COPY . /app/
