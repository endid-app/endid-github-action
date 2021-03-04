FROM python:3-slim
ADD . /app
WORKDIR /app

RUN pip install endid

ENV PYTHONPATH /app
CMD ["/app/main.py"]
