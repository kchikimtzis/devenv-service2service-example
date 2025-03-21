from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Dapr sidecar URL (local or cluster)
DAPR_HOST = "http://localhost:3500"
SERVICE_B_ID = "service-b"
DAPR_URL = "http://service-a-dapr.default.svc.cluster.local:3500"


@app.route("/")
def home():
    return "Flask App with Dapr Running!"

@app.route("/invoke-service-b", methods=["POST"])
def invoke_service_b():
    data = request.json
    print(data)
    dapr_url = f"{DAPR_HOST}/v1.0/invoke/{SERVICE_B_ID}/method/process"
    
    response = requests.post(dapr_url, json=data)
    return response.json(), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
