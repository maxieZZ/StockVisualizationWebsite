# build using the following command
# >> 	docker build -t django-docker .

 use official Python runtime image
FROM python:3.13 # selects image with required python version
 
# create the app directory
RUN mkdir /app 
 
# set working directory of the app within the container 
WORKDIR /app
 
# Set environment variables needed to build app
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container
COPY . /app/
 
# expose the Django server port
EXPOSE 8000
 
# run Django’s development server by defining startup command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]