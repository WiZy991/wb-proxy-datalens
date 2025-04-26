from flask import Flask, jsonify, request, Response
import requests
import os
import csv
import io

app = Flask(__name__)

# Вставь сюда свой токен или используй переменные окружения
WB_TOKEN = os.getenv("WB_TOKEN", "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjUwMjE3djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc2MDU3OTM2MCwiaWQiOiIwMTk2M2VkYy04MDg1LTdhMTYtYjllMS1hYmRlNzE2ZWMwZDUiLCJpaWQiOjI3ODY4NjAyLCJvaWQiOjEyMTA4ODYsInMiOjEwNzM3NDE4NTYsInNpZCI6IjgxOWMxZjQ2LTU0ODMtNDc0ZS05ZjM1LTlhZWUxNWM2MTQ1MyIsInQiOmZhbHNlLCJ1aWQiOjI3ODY4NjAyfQ.MbJIqS_lsQmOa00ktQt3FqEMvONJz10ZDQQqAIjGUVJhFnFaHtslV55BWC6fRyKBPzNTwEqlmwHxbD6AXFUcHg")

@app.route('/')
def home():
    return "\u2705 WB Proxy API is working"

@app.route('/wb/sales-csv')
def get_sales_csv():
    date_from = request.args.get('dateFrom')
    if not date_from:
        return "dateFrom is required (format YYYY-MM-DD)", 400

    headers = {"Authorization": f"Bearer {WB_TOKEN}"}
    url = f"https://statistics-api.wildberries.ru/api/v1/supplier/sales?dateFrom={date_from}"
    try:
        response = requests.get(url, headers=headers)
        if not response.ok:
            return f"Error from WB: {response.text}", response.status_code

        data = response.json()
        if not data:
            return "No data available", 204

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

        return Response(output.getvalue(), mimetype="text/csv")

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
