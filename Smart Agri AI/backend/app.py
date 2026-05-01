from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import os
import requests
import numpy as np

app = FastAPI(title="Smart Agriculture API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Models
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")
MARKET_DATA_PATH = os.path.join(os.path.dirname(__file__), "model", "market_data.pkl")

try:
    model = joblib.load(MODEL_PATH)
    market_data = joblib.load(MARKET_DATA_PATH)
except Exception as e:
    print("Warning: Models not found or failed to load. Please run train_model.py first.")
    model = None
    market_data = {}

# Pydantic models for input validation
class SoilAnswers(BaseModel):
    color: str
    texture: str
    water_retention: str
    previous_crop: str = ""

class Location(BaseModel):
    lat: float
    lon: float

class PredictRequest(BaseModel):
    soil_answers: SoilAnswers
    location: Location
    # weather can be passed or we fetch it. We will fetch it using location.
    
class PredictResponse(BaseModel):
    estimated_soil: dict
    weather: dict
    best_crop: str
    top_profitable_crops: list

# OpenWeatherMap API details
# Replace with your own API key
WEATHER_API_KEY = "bd5e378503939ddaee76f12ad7a97608" # Placeholder API Key

def fetch_weather(lat, lon):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Estimate rainfall (if not present in weather, default to 100 for simplicity)
        rainfall = data.get("rain", {}).get("1h", 0) * 24 * 30 # Rough monthly estimate
        if rainfall == 0:
            rainfall = np.random.uniform(50, 150) # Fallback heuristic
            
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rainfall": rainfall
        }
    except Exception as e:
        print(f"Weather fetch failed: {e}")
        # Fallback values
        return {"temp": 25.0, "humidity": 70.0, "rainfall": 100.0}

def estimate_npk_ph(answers: SoilAnswers):
    # Base values
    N, P, K, pH = 50, 50, 50, 6.5
    
    color = answers.color.lower()
    texture = answers.texture.lower()
    retention = answers.water_retention.lower()
    
    # Heuristics based on color
    if color == "black":
        N, P, K, pH = 100, 60, 80, 7.5
    elif color == "red":
        N, P, K, pH = 40, 30, 40, 6.5
    elif color == "brown":
        N, P, K, pH = 80, 50, 60, 7.0
    elif color == "sandy":
        N, P, K, pH = 30, 20, 20, 6.0
        
    # Adjustments based on texture
    if texture == "sticky":
        pH += 0.2
    elif texture == "grainy":
        N -= 10
        K -= 10
        pH -= 0.2
        
    # Adjustments based on water retention
    if retention == "high":
        N += 10
    elif retention == "low":
        N -= 10
        P -= 5
        
    return {"N": N, "P": P, "K": K, "pH": pH}

@app.post("/predict", response_model=PredictResponse)
def predict_crop(req: PredictRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Train the model first.")
        
    # 1. Fetch Weather
    weather = fetch_weather(req.location.lat, req.location.lon)
    
    # 2. Estimate Soil
    soil = estimate_npk_ph(req.soil_answers)
    
    # 3. Predict Best Crop
    # Features order: ["N", "P", "K", "pH", "Temp", "Hum", "Rain"]
    features = np.array([[
        soil["N"], soil["P"], soil["K"], soil["pH"],
        weather["temp"], weather["humidity"], weather["rainfall"]
    ]])
    
    best_crop = model.predict(features)[0]
    
    # 4. Recommend Top 3 Profitable Crops
    # Use predict_proba to get top 3 likely crops suitable for this soil/weather
    probs = model.predict_proba(features)[0]
    classes = model.classes_
    
    # Sort by probability
    top_indices = np.argsort(probs)[::-1][:5] # Get top 5 candidates
    candidates = [classes[i] for i in top_indices]
    
    # Calculate expected profit for candidates
    profits = []
    for c in candidates:
        if c in market_data:
            m = market_data[c]
            # Profit = Yield * Price (simplified)
            profit = m["avg_yield"] * m["avg_price"]
            profits.append({"crop": c, "estimated_profit": round(profit, 2)})
            
    # Sort by profit and pick top 3
    profits = sorted(profits, key=lambda x: x["estimated_profit"], reverse=True)[:3]
    
    return PredictResponse(
        estimated_soil=soil,
        weather=weather,
        best_crop=best_crop,
        top_profitable_crops=[p["crop"] for p in profits]
    )

# Mount the frontend static files at the root
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
