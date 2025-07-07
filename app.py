from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulasi database kode lisensi
DATABASE = {
    "ABC1234": "2025-08-31",
    "VIP9999": "2099-12-31",
    "TEST999": "2025-12-31"
}

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    kode = data.get("kode", "").strip()
    if not kode or kode not in DATABASE:
        return jsonify({"valid": False, "reason": "Kode tidak ditemukan"}), 200

    try:
        exp = datetime.strptime(DATABASE[kode], "%Y-%m-%d")
        if exp < datetime.now():
            return jsonify({"valid": False, "reason": "Lisensi kedaluwarsa"}), 200
        return jsonify({"valid": True, "expired_at": DATABASE[kode]}), 200
    except:
        return jsonify({"valid": False, "reason": "Format data salah"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
