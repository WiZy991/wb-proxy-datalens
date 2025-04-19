from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

WB_TOKEN = os.getenv("eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjUwMjE3djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc2MDU3OTM2MCwiaWQiOiIwMTk2M2VkYy04MDg1LTdhMTYtYjllMS1hYmRlNzE2ZWMwZDUiLCJpaWQiOjI3ODY4NjAyLCJvaWQiOjEyMTA4ODYsInMiOjEwNzM3NDE4NTYsInNpZCI6IjgxOWMxZjQ2LTU0ODMtNDc0ZS05ZjM1LTlhZWUxNWM2MTQ1MyIsInQiOmZhbHNlLCJ1aWQiOjI3ODY4NjAyfQ.MbJIqS_lsQmOa00ktQt3FqEMvONJz10ZDQQqAIjGUVJhFnFaHtslV55BWC6fRyKBPzNTwEqlmwHxbD6AXFUcHg")  # Временно можешь вставить токен сюда

@app.route('/')
def home():
    return "✅ WB Proxy API is running"

@app.route('/wb/stocks')
def get_stocks():
    headers = {"Authorization": f"Bearer {WB_TOKEN}"}
    url = "https://statistics-api.wildberries.ru/api/v1/supplier/stocks"
    response = requests.get(url, headers=headers)
    
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Ошибка от WB", "details": response.text}), response.status_code

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # ☑️ Render укажет PORT как переменную окружения
    app.run(host='0.0.0.0', port=port)
