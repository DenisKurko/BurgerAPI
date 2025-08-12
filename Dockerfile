FROM python:3.13.2

WORKDIR /

COPY /app /app
COPY requirements/dev.txt requirements/dev.txt

RUN pip install --no-cache-dir -r requirements/dev.txt

CMD [ "python", "app/main.py" ]