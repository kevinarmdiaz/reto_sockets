  
FROM python:3.8.4-slim-buster
ADD client_tornado.py /
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

CMD ["python","-u","client_tornado.py"]