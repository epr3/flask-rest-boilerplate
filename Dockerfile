FROM python:3.7

WORKDIR /database

RUN touch ./db.sqlite

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install pipenv

RUN pipenv install --pre -r requirements.txt

ADD . .

RUN pipenv run flask db upgrade
