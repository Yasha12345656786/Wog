# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

COPY Scores.txt /Scores.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]


# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV FLASK_APP=app.py

# Run the Flask app
CMD ["MainScores.py"]