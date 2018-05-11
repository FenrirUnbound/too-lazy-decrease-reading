FROM python:3 AS build

WORKDIR /usr/src/app
COPY app /usr/src/app
COPY start_server /usr/src/app/start_server

RUN rm -rf test venv \
    && pip install virtualenv \
    && virtualenv venv \
    && . venv/bin/activate \
    && pip install -Ur requirements.txt \
    && touch venv/bin/activate \
    && chmod +x venv/bin/activate

FROM python:3-slim

COPY --from=build /usr/src/app /usr/src/app

WORKDIR /usr/src/app
ENV PYTHONPATH="/usr/src/app/venv:${PYTHONPATH}"
RUN . venv/bin/activate \
  && python -c "import nltk; nltk.download('punkt')" \
  && mv /usr/src/app/start_server /usr/local/bin


ENTRYPOINT [ "/usr/local/bin/start_server" ]