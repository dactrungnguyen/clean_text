FROM python:3.7-slim
WORKDIR /usr/src/app
COPY src/back src/back
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "-m", "src.back"]
