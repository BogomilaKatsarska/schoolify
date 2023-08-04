FROM python:3.10

RUN apt update -y \
    && apt upgrade -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENV HOME=C:\home\app
ENV APP_HOME=C:\home\app\web
ENV STATICFILES_HOME=C:\tmp\staticfiles
RUN mkdir -p $STATICFILES_HOME

WORKDIR $APP_HOME

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .