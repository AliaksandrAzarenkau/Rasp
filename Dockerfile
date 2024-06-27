FROM python:3.10

RUN mkdir /fastapi-app

WORKDIR /fastapi-app

COPY requirements/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src

CMD gunicorn main:app --bind=0.0.0.0:8000
