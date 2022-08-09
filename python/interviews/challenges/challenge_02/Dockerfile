FROM python:3.8.13-slim

COPY question_3 .
COPY question_5/gunicorn.conf.py .


RUN pip install --no-cache-dir --disable-pip-version-check --trusted-host pypi.org -r requirements.txt gunicorn[gthread]==20.0.4

CMD exec gunicorn -c ./gunicorn.conf.py app:app