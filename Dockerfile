FROM python:3.12-slim

WORKDIR /app

COPY main.py .
COPY treinos.json .

CMD ["python", "main.py"]