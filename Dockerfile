FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY main.py ./

#ENTRYPOINT ["python"]

CMD ["python", "main.py"]

EXPOSE 5000/tcp

