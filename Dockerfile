FROM python:3-alpine3.13

WORKDIR /app

COPY . /app

RUN pip install flask
RUN pip install flask-mysql 
RUN pip install -U flask-cors

EXPOSE 8082

CMD ["python3", "main.py"]
