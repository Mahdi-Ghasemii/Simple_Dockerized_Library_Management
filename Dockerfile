FROM python:3

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python3 utils/db.py

EXPOSE 5001

CMD ["python3" , "app.py" , "host=0.0.0.0" , "-p" , "3000"]