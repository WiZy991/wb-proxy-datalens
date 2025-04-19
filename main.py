from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Авторизационный токен WB — подставь свой токен или используй переменные окружения
WB_TOKEN = os.getenv("eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjUwMjE3djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc2MDU3OTM2MCwiaWQiOiIwMTk2M2VkYy04MDg1LTdhMTYtYjllMS1hYmRlNzE2ZWMwZDUiLCJpaWQiOjI3ODY4NjAyLCJvaWQiOjEyMTA4ODYsInMiOjEwNzM3NDE4NTYsInNpZCI6IjgxOWMxZjQ2LTU0ODMtNDc0ZS05ZjM1LTlhZWUxNWM2MTQ1MyIsInQiOmZhbHNlLCJ1aWQiOjI3ODY4NjAyfQ.MbJIqS_lsQmOa00ktQt3FqEMvONJz10ZDQQqAIjGUVJhFnFaHtslV55BWC6fRyKBPzNTwEqlmwHxbD6AXFUcHg")  # ← вставь сюда свой токен по умолчанию

# Пример запроса к API Wildberries — остатки на складе
@app.route('/wb/stocks', methods=['GET'])
def get_wb_stocks():
    headers = {"Authorization": f"Bearer {WB_TOKEN}"}
    url = "https://statistics-api.wildberries.ru/api/v1/supplier/stocks"
    response = requests.get(url, headers=headers)
    
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Ошибка при получении данных", "details": response.text}), response.status_code

# Для проверки
@app.route('/')
def hello():
    return "WB Proxy API is working."

if __name__ == '__main__':
    app.run(debug=True)
