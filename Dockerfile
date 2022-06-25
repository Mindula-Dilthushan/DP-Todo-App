FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY main.py ./

#ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["python", "main.py"]