# syntax = docker/dockerfile:experimental

ARG PYTHON_VERSION=3.8.7
FROM python:${PYTHON_VERSION}-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.10

WORKDIR /app

# Install poetry (package manager) and disable virtual environment
RUN python -m pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.create false

# Install python package dependencies
COPY poetry.lock pyproject.toml ./
# TODO: remove --dev for production image
RUN poetry export -f requirements.txt --dev | pip install -r /dev/stdin

# Install source code
COPY ./ app/

CMD ["bash"]
