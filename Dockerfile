FROM python:3.8
RUN mkdir code
COPY ./src /code
WORKDIR /code
COPY requirements.txt .
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "app.py"]