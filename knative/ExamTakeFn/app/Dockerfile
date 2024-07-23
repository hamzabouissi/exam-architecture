# 
FROM python:3.11

RUN pip install --upgrade pip
# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --timeout=1000 -r /code/requirements.txt

# 
COPY ./ /code/app

# 
CMD ["fastapi", "run", "app/app.py", "--port", "80"]