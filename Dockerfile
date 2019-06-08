FROM python:3.6
WORKDIR /app
RUN pip install bottle
COPY app.py /app
CMD ["python3", "app.py"]