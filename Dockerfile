FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["app.py"]