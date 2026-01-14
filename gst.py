from flask import Flask, jsonify

app = Flask(__name__)

GST_DATA = [
    {"category": "Electronics", "gst_percent": 18},
    {"category": "Clothing", "gst_percent": 12},
    {"category": "Food", "gst_percent": 5},
    {"category": "Furniture", "gst_percent": 28}
]

@app.route("/gst-rates", methods=["GET"])
def gst_rates():
    return jsonify(GST_DATA)

if __name__ == "__main__":
    app.run()
