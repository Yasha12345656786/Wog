FROM python:3.12-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

COPY Scores.txt /Scores.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["MainScores.py"]