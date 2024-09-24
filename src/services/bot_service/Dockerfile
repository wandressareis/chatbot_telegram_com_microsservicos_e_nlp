FROM python:3.10-slim

WORKDIR /bot_service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]

#CMD ["uvicorn", "app.db:app", "--host", "0.0.0.0", "--port", "8001"]