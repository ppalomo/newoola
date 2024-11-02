# FROM python:3.10
FROM python:3.11-alpine

WORKDIR /code

# Install the package dependencies in the requirements file.
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

EXPOSE 8000

# CMD ["fastapi", "run", "src/main.py"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]