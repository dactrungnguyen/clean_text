FROM python:3.7-slim
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /usr/app
COPY src/back src/back
COPY src/front src/front
CMD ["python", "-m", "src.api"]
