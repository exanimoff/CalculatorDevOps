FROM python:3.8.17-slim-bookworm

WORKDIR /app

COPY Calculator.py .
ENTRYPOINT ["python"]
CMD ["Calculator.py"]