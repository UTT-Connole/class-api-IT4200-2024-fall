FROM python:3.9-slim


EXPOSE 5000
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY __init__.py __init__.py
COPY templates templates
COPY endpoints endpoints
COPY static static
COPY app.py app.py

ENV WEATHER_API_KEY=$WEATHER_API_KEY

CMD ["python", "app.py"]