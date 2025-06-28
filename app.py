from flask import Flask, request, jsonify
import requests
import os

app = Flask(_name_)

# Replace these with your actual Gupshup credentials
GUPSHUP_API_URL = "https://api.gupshup.io/sm/api/v1/msg"
GUPSHUP_APP_NAME = "your-app-name"
GUPSHUP_API_KEY = "your-gupshup-api-key"
WHATSAPP_NUMBER = "919819555235"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", "Stock Alert Triggered!")
    
    payload = {
        "channel": "whatsapp",
        "source": GUPSHUP_APP_NAME,
        "destination": WHATSAPP_NUMBER,
        "message": message,
        "src.name": GUPSHUP_APP_NAME
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey": GUPSHUP_API_KEY
    }

    response = requests.post(GUPSHUP_API_URL, data=payload, headers=headers)
    return jsonify({"status": response.status_code, "response": response.text})

if _name_ == "_main_":
    app.run(debug=True)
