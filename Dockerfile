FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY . .
RUN pip install -r requirements.txt
WORKDIR .
EXPOSE 8080

# ENV SERVER_NAME="grpc-server"

# 相当于执行 uvicorn main:app --host 0.0.0.0 --port 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "8080"]

