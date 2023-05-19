FROM python:3.11

WORKDIR /opt/app

ENV PYTHONPATH '/opt/app'

COPY requirements.txt requirements.txt

RUN  python -m pip install --no-cache-dir --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY . .

# Start the app using Gunicorn и Uvicorn Worker
#CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]