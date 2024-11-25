FROM python:3.13.0a1-alpine3.18

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./* /app/

RUN cd app

CMD [ "python app.py" ]