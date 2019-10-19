FROM python:3-alpine
ADD request.py /
RUN pip install -r requirements.txt
CMD [ "python", "./request.py" ]