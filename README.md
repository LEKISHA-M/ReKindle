# ⚡ ReKindle — Smart Kitchen Energy Dashboard

> Transforming kitchen waste gas into reusable energy — powered by AI.

🔗 Live Demo: fetch("https://rekindle-production-dc32.up.railway.app/sensor")

---

## 🌍 Problem Statement

Every day, kitchens waste significant amounts of cooking gas through leaks, incomplete combustion, and chimney exhaust. At the same time, organic waste under the sink produces biogas that goes unused. ReKindle addresses both problems by monitoring, predicting, and helping reuse this wasted energy.

---

## 💡 Solution

ReKindle is a smart kitchen energy monitoring system that:

- 📡 Monitors kitchen gas levels and temperature in real time via sensors
- 🤖 Predicts gas leak risk using AI based on time-of-day cooking patterns
- ♻️ Tracks biogas collected from under-sink organic waste
- 💰 Calculates energy saved, monthly cost savings, and carbon footprint reduced
- 🚨 Alerts users when dangerous gas levels are detected

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Front End | HTML, CSS, JavaScript |
| Back End | Python, Flask |
| AI Prediction | Python (ai_predict.py) |
| Frontend Deployment | Vercel |
| Backend Deployment | Railway |

---

## 🤖 AI Prediction Logic

| Time of Day | Risk Level | Reason |
|-------------|------------|--------|
| 6 AM – 9 AM | HIGH | Morning cooking peak |
| 12 PM – 2 PM | HIGH | Lunch peak |
| 6 PM – 9 PM | MEDIUM | Evening cooking |
| Other times | LOW | Low activity |

---

## 📊 Dashboard Features

- ✅ System Status — Normal / Danger
- 🤖 AI Prediction — Real-time risk level and advice
- 💨 Gas Level (ppm) — Live sensor reading
- 🌡️ Temperature (°C) — Kitchen temperature
- ⚡ Energy Saved (kWh) — Cumulative savings
- 🔥 Biogas Produced (L) — Collected biogas volume
- 💵 Monthly Savings (₹) — Financial impact
- 🌱 Carbon Reduced (kg) — Environmental impact
- 🚨 Gas Leak Simulation — Demo safety alert system

---

## 📁 Project Structure

    rekindle/
    ├── app.py
    ├── ai_predict.py
    ├── simulator.py
    ├── dashboard.html
    ├── index.html
    ├── requirements.txt
    └── Procfile.txt
    
---

## 🌱 Impact

- Reduces kitchen gas wastage
- Promotes biogas reuse from organic waste
- Saves money on monthly fuel bills
- Lowers household carbon footprint
- Provides early warning for dangerous gas leaks

---

## 👨‍💻 Built for

Online Hackathon 2026 — Smart Energy & Sustainability Track
