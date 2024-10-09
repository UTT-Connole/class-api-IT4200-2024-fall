FROM python:3.9-slim


EXPOSE 5000
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY __init__.py __init__.py
COPY templates templates
COPY endpoints endpoints
COPY app.py app.py


CMD ["python", "app.py"]