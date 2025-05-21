FROM python:3.12-slim as base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off

WORKDIR /app

ENV PATH="/root/.local/bin:$PATH"

RUN set -ex \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
       make \
       build-essential \
       zlib1g-dev \
       libjpeg-dev \
       libpng-dev \
    && pip install poetry==1.6.1 \
    && poetry config virtualenvs.create false \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/

RUN set -ex \
    && poetry install $(test "$BUILD_ENV" = production && echo "--no-dev") --no-root --no-interaction --no-ansi

FROM base as full

COPY . /app/
