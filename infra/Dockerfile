FROM python:3.7-slim
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY src/back src/back
COPY src/api src/api
COPY src/front src/front
EXPOSE 5000
CMD ["python", "-m", "src.api"]
