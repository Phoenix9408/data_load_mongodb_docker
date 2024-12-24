FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY Loading_app/src/ ./src/

RUN ls -R /app

CMD ["python", "./src/migrating_job.py"]


