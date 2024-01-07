FROM python:3.7-alpine
RUN addgroup -S app && adduser app -S -G app

# Set Working directory
WORKDIR /app

# Copy files from src to dest
COPY src/ .

# Using root user
USER root

# Make sure all requirements are installed
RUN pip install -r requirements.txt

RUN chown -R app:app ./

USER app

CMD ["python3", "./app.py"]
