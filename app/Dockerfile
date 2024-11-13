FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY utils /app/utils

COPY . .

CMD [ "./run_flask.sh" ] 