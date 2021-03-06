FROM openfaas/classic-watchdog:0.18.1 as watchdog

FROM python:3.7-slim

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

WORKDIR /usr/app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/back src/back

ENV fprocess="python -m src.back"

CMD [ "fwatchdog" ]