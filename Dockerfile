FROM python:3-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD [ "request.py" ]
# Change this CMD to either run request.py or request_test.py