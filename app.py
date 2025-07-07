from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    kode = data.get("kode")

    with open("database.json") as f:
        db = json.load(f)

    if kode not in db:
        return jsonify({"valid": False, "reason": "Kode tidak ditemukan"}), 200

    exp_str = db[kode]
    exp_date = datetime.strptime(exp_str, "%Y-%m-%d")
    if exp_date < datetime.now():
        return jsonify({"valid": False, "reason": "Masa berlaku habis"}), 200

    return jsonify({
        "valid": True,
        "expired_at": exp_str
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
