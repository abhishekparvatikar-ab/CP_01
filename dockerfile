FROM python:3.14

WORKDIR /app

COPY employee.py .

CMD ["python", "employee.py"]