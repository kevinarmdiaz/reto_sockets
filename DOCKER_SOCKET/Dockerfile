  
FROM python:3.8.4-slim-buster
ADD server.py /
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

CMD ["python","-u","server.py"]
