import random
import time
import json
from datetime import datetime

sensor_data = []

def simulate_sensor():
    gas_level = round(random.uniform(200, 800), 2)
    temperature = round(random.uniform(25, 45), 2)
    leak_detected = gas_level > 600
    
    data = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "gas_level": gas_level,
        "temperature": temperature,
        "leak_detected": leak_detected,
        "status": "DANGER" if leak_detected else "NORMAL"
    }
    
    sensor_data.append(data)
    print(f"[{data['timestamp']}] Gas: {gas_level} ppm | Temp: {temperature}°C | Status: {data['status']}")
    return data

print("ReKindle Sensor Simulator Started...")
print("Press Ctrl+C to stop\n")

while True:
    simulate_sensor()
    time.sleep(2)