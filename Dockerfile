FROM python:3.13.2-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn  # Ensure gunicorn is installed

COPY . /app/

CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]