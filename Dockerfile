FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

# Copy source files into docker
COPY . .

EXPOSE 8000

CMD ["python", "src/s3-file-uploader/manage.py", "migrate"]

CMD ["python", "src/s3-file-uploader/manage.py", "runserver", "0.0.0.0:8000"]
