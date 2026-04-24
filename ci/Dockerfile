FROM python:3.12

WORKDIR /app

COPY src src
COPY screenshots screenshots
COPY pytest.ini .
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN playwright install chrome

CMD ["pytest", "-s", "-v"]