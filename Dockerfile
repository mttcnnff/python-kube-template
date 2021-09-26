FROM python:3.9-slim AS compile-image

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -

FROM python:3.9-slim AS runtime-image
COPY --from=compile-image /root/.local/ /root/.local
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY . .

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "uvicorn", "--host=0.0.0.0"]
CMD ["--factory", "spend_api.main:init_app"]