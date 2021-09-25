FROM alpine:latest
ARG PYTHON_VERSION=3.9.2


RUN apk update
RUN apk add bash bash-completion curl git build-base patch zip zlib-dev libffi-dev linux-headers readline-dev openssl openssl-dev sqlite-dev bzip2-dev

RUN curl https://pyenv.run | bash
ENV PATH="/root/.pyenv/shims:/root/.pyenv/bin:$PATH"
RUN eval "$(pyenv init -)"
RUN eval "$(pyenv virtualenv-init -)"

RUN pyenv install ${PYTHON_VERSION}
RUN pyenv global ${PYTHON_VERSION}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH="/root/.local/bin:$PATH"


WORKDIR /app
COPY . .
RUN poetry install


EXPOSE 8000
ENTRYPOINT ["poetry", "run", "uvicorn", "--host=0.0.0.0"]
CMD ["--factory", "spend_api.main:init_app"]