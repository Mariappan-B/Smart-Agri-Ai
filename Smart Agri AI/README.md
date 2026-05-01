# Smart Agriculture Web Application

An AI-based smart agriculture system that predicts the best crop and recommends profitable alternatives based on soil heuristics and real-time weather data. 

## Features
- **User-friendly Input**: No need to know exact NPK values or pH. Just input soil color, texture, and water retention.
- **Location & Weather**: Automatically fetches real-time temperature, humidity, and estimates rainfall using the OpenWeatherMap API.
- **Machine Learning**: Uses a `RandomForestClassifier` trained on a synthetic dataset to predict the best crop.
- **Profitability Recommendations**: Recommends the top 3 alternative crops based on estimated yield and market prices.
- **Modern UI**: A responsive, vibrant, and glassmorphism-styled single-page web interface.

## Tech Stack
- **Frontend**: HTML, CSS (Vanilla), JavaScript (Vanilla)
- **Backend**: Python (FastAPI)
- **Machine Learning**: Scikit-Learn, Pandas, Numpy

## Folder Structure
```
Smart Agri AI/
│
├── backend/
│   ├── app.py                  # FastAPI Application
│   └── model/
│       ├── train_model.py      # ML Data generation & training script
│       ├── model.pkl           # Saved RandomForest model (Generated)
│       └── market_data.pkl     # Saved market metadata (Generated)
│
├── frontend/
│   ├── index.html              # Main web interface
│   ├── style.css               # Modern UI styling
│   └── script.js               # UI logic and API fetching
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── smart_agri_project.zip      # Packaged project (Generated)
```

## Setup Instructions

### 1. Install Dependencies
Make sure you have Python 3 installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Train the Machine Learning Model
Before running the backend, you must generate the synthetic dataset and train the model.
```bash
python backend/model/train_model.py
```
*This will create `model.pkl` and `market_data.pkl` inside the `backend/model/` directory.*

### 3. Run the Backend Server
Start the FastAPI server using Uvicorn:
```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```
*The API will be available at `http://localhost:8000/predict`*

### 4. Open the Frontend
Simply double-click the `frontend/index.html` file in your file explorer to open it in your default web browser.

## Important Notes
- **API Key**: The backend (`backend/app.py`) currently uses a placeholder API key for OpenWeatherMap. If you encounter weather fetching errors, you may need to replace it with your own free API key from [OpenWeatherMap](https://openweathermap.org/api).
- **CORS**: The FastAPI backend is configured to allow requests from any origin (`*`) to ensure the local HTML file can communicate with it easily.
