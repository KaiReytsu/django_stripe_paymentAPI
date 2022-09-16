FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install pipenv
WORKDIR /djangostripe
COPY Pipfile /djangostripe/
RUN pipenv install
COPY . /djangostripe/