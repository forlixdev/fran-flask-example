FROM python:3.11-alpine

COPY . /home
WORKDIR /home
RUN pip install -r requirements.txt

CMD python run.py