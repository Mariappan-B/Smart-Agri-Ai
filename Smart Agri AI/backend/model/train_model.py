import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import os

def generate_synthetic_data(n_samples=5000):
    np.random.seed(42)
    
    crops = [
        "Rice", "Wheat", "Maize", "Cotton", "Sugarcane", 
        "Tomato", "Potato", "Onion", "Soybean", "Groundnut"
    ]
    
    data = []
    
    # Define ideal conditions roughly for each crop
    crop_profiles = {
        "Rice": {"N": (80, 120), "P": (40, 60), "K": (40, 60), "pH": (5.5, 7.0), "Temp": (20, 35), "Hum": (80, 95), "Rain": (150, 300), "Price": (20, 30), "Yield": (4, 6)},
        "Wheat": {"N": (60, 100), "P": (30, 50), "K": (30, 50), "pH": (6.0, 7.5), "Temp": (10, 25), "Hum": (50, 70), "Rain": (50, 100), "Price": (25, 35), "Yield": (3, 5)},
        "Maize": {"N": (80, 120), "P": (40, 60), "K": (40, 60), "pH": (5.8, 7.5), "Temp": (18, 27), "Hum": (60, 80), "Rain": (60, 110), "Price": (15, 25), "Yield": (5, 8)},
        "Cotton": {"N": (100, 140), "P": (40, 60), "K": (40, 60), "pH": (5.8, 8.0), "Temp": (22, 32), "Hum": (50, 70), "Rain": (60, 110), "Price": (50, 70), "Yield": (1, 2)},
        "Sugarcane": {"N": (120, 160), "P": (60, 80), "K": (60, 80), "pH": (6.0, 7.5), "Temp": (20, 35), "Hum": (70, 90), "Rain": (150, 250), "Price": (3, 6), "Yield": (60, 80)},
        "Tomato": {"N": (80, 120), "P": (40, 60), "K": (40, 60), "pH": (6.0, 7.0), "Temp": (20, 30), "Hum": (60, 80), "Rain": (40, 80), "Price": (15, 40), "Yield": (20, 30)},
        "Potato": {"N": (100, 140), "P": (50, 70), "K": (50, 70), "pH": (5.0, 6.5), "Temp": (15, 25), "Hum": (70, 90), "Rain": (50, 100), "Price": (10, 25), "Yield": (15, 25)},
        "Onion": {"N": (80, 120), "P": (40, 60), "K": (40, 60), "pH": (6.0, 7.0), "Temp": (15, 30), "Hum": (50, 70), "Rain": (30, 70), "Price": (15, 35), "Yield": (15, 25)},
        "Soybean": {"N": (20, 60), "P": (40, 60), "K": (40, 60), "pH": (6.0, 7.5), "Temp": (20, 30), "Hum": (60, 80), "Rain": (60, 120), "Price": (35, 55), "Yield": (2, 4)},
        "Groundnut": {"N": (20, 40), "P": (40, 60), "K": (40, 60), "pH": (6.0, 7.5), "Temp": (20, 30), "Hum": (50, 70), "Rain": (50, 100), "Price": (45, 65), "Yield": (1, 3)}
    }
    
    for _ in range(n_samples):
        crop = np.random.choice(crops)
        prof = crop_profiles[crop]
        
        N = np.random.uniform(*prof["N"])
        P = np.random.uniform(*prof["P"])
        K = np.random.uniform(*prof["K"])
        pH = np.random.uniform(*prof["pH"])
        Temp = np.random.uniform(*prof["Temp"])
        Hum = np.random.uniform(*prof["Hum"])
        Rain = np.random.uniform(*prof["Rain"])
        
        # Price and Yield will be used later for profitability, storing them just in case
        Price = np.random.uniform(*prof["Price"])
        Yield = np.random.uniform(*prof["Yield"])
        
        data.append([N, P, K, pH, Temp, Hum, Rain, crop, Price, Yield])
        
    df = pd.DataFrame(data, columns=["N", "P", "K", "pH", "Temp", "Hum", "Rain", "Crop", "Price", "Yield"])
    
    # Save a lightweight version of market data for the backend to use
    market_data = {
        c: {"avg_price": np.mean(crop_profiles[c]["Price"]), "avg_yield": np.mean(crop_profiles[c]["Yield"])} 
        for c in crops
    }
    joblib.dump(market_data, os.path.join(os.path.dirname(__file__), "market_data.pkl"))
    
    return df

def train_and_save_model():
    print("Generating synthetic dataset...")
    df = generate_synthetic_data(n_samples=5000)
    
    X = df[["N", "P", "K", "pH", "Temp", "Hum", "Rain"]]
    y = df["Crop"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training RandomForestClassifier...")
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    pipeline.fit(X_train, y_train)
    
    accuracy = pipeline.score(X_test, y_test)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model()
