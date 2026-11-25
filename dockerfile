FROM python:3.11-slim

WORKDIR /app

COPY Student.py .

CMD ["python", "Student.py"]