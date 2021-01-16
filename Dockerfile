FROM python:3.8.3

COPY ./app /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8080

WORKDIR '/app'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]