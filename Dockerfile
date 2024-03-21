FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

ENV PATH="/root/.local/bin:$PATH" 
ENV PYTHONPATH="/"

COPY ./poetry.lock /
COPY ./pyproject.toml /

RUN apt-get update -y && apt-get install curl -y 
RUN curl -sSL https://install.python-poetry.org | python3 -  
RUN poetry config virtualenvs.create false 
RUN poetry install 
RUN apt-get remove curl -y

WORKDIR /app

COPY ./app /app
COPY ./.env /app
EXPOSE 8000

ENTRYPOINT [ "uvicorn", "app.main:app", "--port=8000", "--host=0.0.0.0", "--reload"]