FROM python:3
WORKDIR /app
COPY . .
RUN pip install flask
ENV APP_HOSTNAME="0.0.0.0"
ENV APP_PORT="8080"
CMD ["python","main.py"]
EXPOSE 8080