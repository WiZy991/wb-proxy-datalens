from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

WB_TOKEN = os.getenv("WB_TOKEN", "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjUwMjE3djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc2MDU3OTM2MCwiaWQiOiIwMTk2M2VkYy04MDg1LTdhMTYtYjllMS1hYmRlNzE2ZWMwZDUiLCJpaWQiOjI3ODY4NjAyLCJvaWQiOjEyMTA4ODYsInMiOjEwNzM3NDE4NTYsInNpZCI6IjgxOWMxZjQ2LTU0ODMtNDc0ZS05ZjM1LTlhZWUxNWM2MTQ1MyIsInQiOmZhbHNlLCJ1aWQiOjI3ODY4NjAyfQ.MbJIqS_lsQmOa00ktQt3FqEMvONJz10ZDQQqAIjGUVJhFnFaHtslV55BWC6fRyKBPzNTwEqlmwHxbD6AXFUcHg")  # Временно можешь вставить токен сюда

@app.route('/')
def home():
    return "✅ WB Proxy API is working. Try /wb/stocks or /wb/sales?dateFrom=2024-01-01"

# Остатки — без параметров
@app.route('/wb/stocks')
def get_stocks():
    headers = {"Authorization": f"Bearer {WB_TOKEN}"}
    url = "https://statistics-api.wildberries.ru/api/v1/supplier/stocks"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

# Продажи — требует dateFrom
@app.route('/wb/sales')
def get_sales():
    date_from = request.args.get('dateFrom')
    if not date_from:
        return jsonify({"error": "Нужно указать параметр ?dateFrom=YYYY-MM-DD"}), 400

    headers = {"Authorization": f"Bearer {WB_TOKEN}"}
    url = f"https://statistics-api.wildberries.ru/api/v1/supplier/sales?dateFrom={date_from}"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

# Заказы — тоже требует dateFrom
@app.route('/wb/orders')
def get_orders():
    date_from = request.args.get('dateFrom')
    if not date_from:
        return jsonify({"error": "Нужно указать параметр ?dateFrom=YYYY-MM-DD"}), 400

    headers = {"Authorization": f"Bearer {WB_TOKEN}"}
    url = f"https://statistics-api.wildberries.ru/api/v1/supplier/orders?dateFrom={date_from}"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

# Поставки — без параметров
@app.route('/wb/incomes')
def get_incomes():
    headers = {"Authorization": f"Bearer {WB_TOKEN}"}
    url = "https://statistics-api.wildberries.ru/api/v1/supplier/incomes"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)



