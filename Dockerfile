FROM python:3.9-slim

RUN apt-get update && apt-get install -y git

EXPOSE 5000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ARG WEATHER_API_KEY
ENV WEATHER_API_KEY=${WEATHER_API_KEY}

ARG VERSION
ENV VERSION=$VERSION

COPY .git .git
COPY __init__.py __init__.py
COPY templates templates
COPY endpoints endpoints
COPY images images
COPY static static
COPY app.py app.py
COPY items.json items.json
COPY test test



CMD ["python", "app.py"]