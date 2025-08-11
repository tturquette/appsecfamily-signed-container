FROM python:3.13.6-alpine3.21

WORKDIR /usr/src/app

# install dependencies
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app ./app

WORKDIR /usr/src/app/app

EXPOSE 8080

CMD ["python", "app.py"]
