FROM python:3-alpine
COPY . /request.py
WORKDIR /request.py
ENTRYPOINT ["python"]
RUN pip install -r requirements.txt
CMD [ "./request.py" ]