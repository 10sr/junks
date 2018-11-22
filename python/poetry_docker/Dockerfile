FROM python:3

# Django not work without this!
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /root/app
WORKDIR /root/app

RUN pip3 install "poetry>=0.12"
#RUN POETRY_VERSION=0.12.9 curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3
#ENV PATH=/root/.poetry/bin:$PATH
#RUN python --version && poetry --version
RUN poetry config settings.virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction -vvv
# TODO: Ignore .venv
COPY . .

ENTRYPOINT ["poetry", "run"]
CMD ["python3"]
