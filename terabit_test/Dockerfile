FROM python:3.11

WORKDIR /terabit_test

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD python manage.py migrate && \
    python create_superuser.py && \
    python manage.py runserver 0.0.0.0:8000
