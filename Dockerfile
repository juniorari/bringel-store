FROM python:3.12.0

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip 
# RUN python -m pip install django-oauth-toolkit 
# RUN pip install faker
# RUN pip install celery
# RUN pip install redis
RUN pip install -r requirements.txt


# Expose port
EXPOSE 8888

# entrypoint to run the bringel.sh file
# ENTRYPOINT ["/app/bringel.sh"]
