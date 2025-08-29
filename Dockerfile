FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "portscanner.main", "scan", "--target", "scanme.nmap.org", "--ports", "1-100", "--engine", "socket"]
