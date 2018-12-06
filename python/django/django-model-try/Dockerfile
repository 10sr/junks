FROM python:3

ENV NERU_BASE_DIR /root/app

ENV POETRY_VERSION 0.12.9

#SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR $NERU_BASE_DIR

RUN pip3 install "poetry==$POETRY_VERSION"
#RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3
#ENV PATH=/root/.poetry/bin:$PATH
RUN poetry config settings.virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --no-interaction -vvv

COPY app app
COPY proj proj
COPY Makefile manage.py ./

EXPOSE 9099

# TODO: Pass via build argument
#RUN git rev-parse HEAD >git_commit_hash.txt

# Django not work without this!
ENV PYTHONUNBUFFERED 1

# ENTRYPOINT ["poetry", "run"]
# CMD ["./manage.py", "runserver", "0.0.0.0:9099"]
CMD ["make", "migrate", "create_admin_user", "runserver"]
