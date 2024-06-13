FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY utils /app/utils

COPY . .

RUN python3 utils/db.py

CMD ["python3" , "app.py" , "host=0.0.0.0" , "-p" ,"3000" ,"-d"] 