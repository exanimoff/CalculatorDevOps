
FROM python:3.8-windowsservercore

WORKDIR /app

COPY Calculator.py .
ENTRYPOINT ["python"]
CMD ["Calculator.py"]
