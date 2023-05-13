FROM python:3.10.8

WORKDIR /app

RUN apt update && apt upgrade -y
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:7000" ]