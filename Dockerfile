FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3.9 -m venv /app/env
RUN . /app/env/bin/activate
RUN pip install -r /app/requirements.txt

COPY . /app

RUN cd /app/weather_service
RUN python3.9 /app/weather_service/manage.py makemigrations
RUN python3.9 /app/weather_service/manage.py migrate

EXPOSE 8000


CMD [ "python3.9", "weather_service/manage.py", "runserver", "0.0.0.0:8000" ]