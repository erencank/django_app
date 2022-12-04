FROM python:3.10

RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=src/

WORKDIR ${APP_HOME}

COPY pyproject.toml poetry.lock ./

RUN bash -c "poetry install --no-root"

COPY /docker/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

EXPOSE 8000

CMD ["/start"]
