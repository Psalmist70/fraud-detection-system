from flask import Flask, request, jsonify
import joblib
from api.utils import map_time, find_nearest_transaction, get_preloaded_transaction
import os
import pickle

app = Flask(__name__)

# -----------------------------
# LOAD MODEL & SCALER
# -----------------------------
model = pickle.load(open('model/fraud_ensemble_model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

# -----------------------------
# A1: CUSTOM TRANSACTION
# -----------------------------
@app.route('/predict-custom', methods=['POST'])
def predict_custom():
    data = request.get_json()

    try:
        amount = float(data['amount'])
        time_period = data['time']
    except:
        return jsonify({"error": "Invalid input"}), 400

    # Map time
    time_value = map_time(time_period)

    # Find nearest dataset row
    row = find_nearest_transaction(time_value, amount)

    # Extract features
    features = row.drop(['Class', 'distance', 'norm_time', 'norm_amount'], errors='ignore').values

    # Replace with user values
    features[0] = time_value   # Time
    features[-1] = amount      # Amount

    features = features.reshape(1, -1)

    # No Scale
    features_scaled = scaler.transform(features)  # now works for 30 features

    # Predict
    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]

    return jsonify({
        "prediction": "Fraud" if pred == 1 else "Legitimate",
        "probability": float(prob),
        "amount": amount,
        "time": time_period
    })


# -----------------------------
# A2: PRELOADED TRANSACTION
# -----------------------------
@app.route('/predict-selected', methods=['POST'])
def predict_selected():
    data = request.get_json()

    txn_id = data.get('transaction_id')

    row = get_preloaded_transaction(txn_id)

    if row is None:
        return jsonify({"error": "Invalid transaction ID"}), 400

    features = row.drop('Class').values.reshape(1, -1)

    # Scale
    features_scaled = scaler.transform(features)  # now works for 30 features

    # Predict
    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]

    return jsonify({
        "prediction": "Fraud" if pred == 1 else "Legitimate",
        "probability": float(prob),
        "amount": float(row['Amount']),
        "time": float(row['Time'])
    })


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
