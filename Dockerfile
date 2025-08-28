# Use python image
FROM python:3.8.0

# Create app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from writing pyc files to disk
ENV PYTHONUNBUFFERED=1


# Prevents Python from buffering stdout and steerr
RUN pip install --upgrade pip

# Upgrade pip 
COPY requirements.txt /app/

# Copy the Django project and install dependencies (requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Copy entrypoint
#COPY entrypoint.sh /app/entrypoint.sh
#RUN chmod +x /app/entrypoint.sh

# Copy source code
COPY . . 

# Expose the Django port
EXPOSE 8000

# Create DB table and Run Django's develpement server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
#CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "config.wsgi:application"]

