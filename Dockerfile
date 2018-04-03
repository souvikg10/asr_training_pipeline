FROM python:2.7-slim

ENV DOCKER="YES" \
    HOME=/app \
    PYTHON_PACKAGES=/usr/local/lib/python2.7/dist-packages

WORKDIR ${HOME}

COPY . ${HOME}

RUN pip install -r requirements.txt

EXPOSE 5000 5005

VOLUME ["/app"]

CMD python run.py 