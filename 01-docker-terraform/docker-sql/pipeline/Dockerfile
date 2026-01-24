FROM python:3.9-slim

WORKDIR /app

# System deps needed for psycopg2
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*
FROM python:3.9-slim

WORKDIR /app

# System deps needed for psycopg2
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY ingest_data.py ingest_data.py

RUN pip install --no-cache-dir \
    pandas \
    sqlalchemy \
    psycopg2-binary \
    pyarrow \
    click \
    tqdm

ENTRYPOINT ["python", "ingest_data.py"]
