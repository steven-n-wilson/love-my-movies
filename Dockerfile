FROM python:3-alpine
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "request.py" ]