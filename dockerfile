FROM python:3.10-slim-buster

WORKDIR /root/app

COPY . .

RUN pip install -r requirment.txt

CMD ["python", "index.py"]