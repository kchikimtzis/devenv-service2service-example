from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_data():
    data = request.json
    print(f"Received data: {data}")
    return jsonify({"message": "Processed by service-b", "data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
