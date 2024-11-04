FROM python:3.11-alpine

WORKDIR /code

# Install the package dependencies in the requirements file.
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

CMD ["celery", "-A", "src.celery", "worker", "--loglevel=info"]

