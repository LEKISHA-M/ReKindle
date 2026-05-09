import random
from datetime import datetime

def predict_gas_waste():
    hour = datetime.now().hour
    
    # Peak times based on kitchen usage patterns
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
    
    return {
        "current_hour": hour,
        "predicted_gas_level": prediction,
        "risk_level": risk,
        "advice": advice,
        "energy_recoverable": round(prediction * 0.003, 3)
    }

# Test it
result = predict_gas_waste()
print(f"Hour: {result['current_hour']}:00")
print(f"Predicted Gas: {result['predicted_gas_level']} ppm")
print(f"Risk Level: {result['risk_level']}")
print(f"Advice: {result['advice']}")
print(f"Energy Recoverable: {result['energy_recoverable']} kWh")