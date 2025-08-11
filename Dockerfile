FROM python:3.11-slim

WORKDIR /usr/src/app

# install dependencies
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app ./app

WORKDIR /usr/src/app/app

EXPOSE 8080

CMD ["python", "app.py"]
