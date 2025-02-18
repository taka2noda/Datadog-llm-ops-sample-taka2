FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENV DD_TRACE_AGENT_URL=http://host.docker.internal:8136

CMD ["ddtrace-run", "python", "app.py"]