FROM python:latest

WORKDIR /app

COPY Calculator.py .
ENTRYPOINT ["python"]
CMD ["Calculator.py"]