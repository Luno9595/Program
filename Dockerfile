FROM python:latest

RUN pip install psutil

COPY program.py /app/program.py
CMD ["python", "/app/program.py"]
