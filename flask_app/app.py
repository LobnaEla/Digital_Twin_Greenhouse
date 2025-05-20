from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo-db:27017")
client = MongoClient(MONGO_URI)
db = client.greenhouse_db
alerts_collection = db.alerts


@app.route("/alert", methods=["POST"])
def receive_alert():
    alert_data = request.get_json()
    alert_data["timestamp"] = datetime.utcnow().isoformat() + "Z"
    result = alerts_collection.insert_one(alert_data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201


@app.route("/sync", methods=["GET"])
def sync_with_mongodb():
    return jsonify({"status": "Flask server is running and connected to MongoDB!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
