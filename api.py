from flask import Flask, request, jsonify
import uuid
import pandas as pd
import os

app = Flask(__name__)

def validate_csv(file):
    """Validates the uploaded CSV file format."""
    required_columns = {"Serial Number", "Product Name", "Image URLs"}
    df = pd.read_csv(file)
    if not required_columns.issubset(df.columns):
        return False, "CSV format incorrect. Required columns: Serial Number, Product Name, Image URLs"
    return True, df

@app.route("/upload_csv", methods=["POST"])
def upload_csv():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    
    is_valid, result = validate_csv(file)
    if not is_valid:
        return jsonify({"error": result}), 400
    
    request_id = str(uuid.uuid4())
    return jsonify({"request_id": request_id, "message": "CSV uploaded successfully. Processing started."})

@app.route("/status/<request_id>", methods=["GET"])
def check_status(request_id):
    return jsonify({"request_id": request_id, "status": "Processing"})

if __name__ == "__main__":
    app.run(debug=True)