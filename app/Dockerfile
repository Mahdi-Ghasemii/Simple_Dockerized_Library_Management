FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY utils /app/utils

# RUN chmod +x wait-for-it.sh

COPY . .

# RUN sudo ./wait.sh
# RUN python3 utils/db.py


CMD ["python3" , "app.py" , "host=0.0.0.0" , "-p" ,"3000" ,"-d"] 

# CMD ["./wait-for-it.sh" , "-t" , "40" , "mysql:3306" ,"--python3" ,"./app.py"] 