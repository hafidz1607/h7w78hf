from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

DATABASE = {
    "ABC1234": "2025-08-31",
    "VIP9999": "2099-12-31"
}

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    kode = data.get("kode", "").strip()
    if not kode or kode not in DATABASE:
        return jsonify({"valid": False, "reason": "Kode tidak ditemukan"}), 200

    expired = datetime.strptime(DATABASE[kode], "%Y-%m-%d")
    if expired < datetime.now():
        return jsonify({"valid": False, "reason": "Lisensi kedaluwarsa"}), 200

    return jsonify({"valid": True, "expired_at": DATABASE[kode]}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
