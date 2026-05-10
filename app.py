import os
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import random
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_sensor_reading():
    gas_level = round(random.uniform(200, 800), 2)
    temperature = round(random.uniform(25, 45), 2)
    leak_detected = gas_level > 600
    return {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "gas_level": gas_level,
        "temperature": temperature,
        "leak_detected": leak_detected,
        "status": "DANGER" if leak_detected else "NORMAL",
        "energy_saved": round(random.uniform(0.5, 2.5), 2),
        "biogas_produced": round(random.uniform(0.1, 0.8), 2)
    }

@app.route('/')
def home():
    return jsonify({"message": "ReKindle API Running!", "version": "1.0"})
@app.route('/predict')
def predict():
    hour = datetime.now().hour
    if 6 <= hour <= 9:
        risk = "HIGH"
        prediction = round(random.uniform(650, 800), 2)
        advice = "Morning cooking peak! Monitor closely."
    elif 12 <= hour <= 14:
        risk = "HIGH"
        prediction = round(random.uniform(600, 750), 2)
        advice = "Lunch peak detected! Check gas valves."
    elif 18 <= hour <= 21:
        risk = "VERY HIGH"
        prediction = round(random.uniform(700, 850), 2)
        advice = "Dinner peak! Maximum gas recovery mode."
    else:
        risk = "LOW"
        prediction = round(random.uniform(200, 400), 2)
        advice = "Off-peak hours. Normal monitoring."
    return jsonify({
        "hour": hour,
        "predicted_gas": prediction,
        "risk_level": risk,
        "advice": advice
    })
@app.route('/sensor')
def sensor():
    return jsonify(get_sensor_reading())

@app.route('/stats')
def stats():
    return jsonify({
        "daily_gas_saved": round(random.uniform(10, 25), 2),
        "monthly_savings": round(random.uniform(150, 400), 2),
        "carbon_reduced": round(random.uniform(2, 8), 2),
        "biogas_total": round(random.uniform(5, 15), 2)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)