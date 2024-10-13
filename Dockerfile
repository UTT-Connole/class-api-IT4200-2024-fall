FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ /app/src

ENV WEATHER_API_KEY=$WEATHER_API_KEY
ENV PYTHONPATH=/app/src

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]