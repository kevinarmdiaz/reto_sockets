FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirementslocal.txt /code/
RUN pip install -r requirementslocal.txt
COPY . /code/
