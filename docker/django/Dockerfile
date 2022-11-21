FROM revolutionsystems/python:3.11.0-wee-optimized-lto

WORKDIR /app 

ENV PYTHONUNBUFFERED 1

RUN python3.11 -m pip install -U pip setuptools

COPY requirements.txt /tmp/requirements.txt 

RUN python3.11 -m pip install -U --no-cache-dir -r /tmp/requirements.txt 

COPY docker/django/entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh 

ENTRYPOINT ["entrypoint.sh"] 
