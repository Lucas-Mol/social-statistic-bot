FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN source social-statistic-bot/bin/activate
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "bot.py"]
