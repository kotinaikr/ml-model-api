from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import joblib
import pandas as pd
import os

app = FastAPI(
    title="Housing Price Prediction API",
    description="Task 1 API for predicting house prices."
)

# Load the trained model on startup
MODEL_PATH = "model.joblib"
model_artifact = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

# Define the expected input payload matching our dataset columns
class HouseFeatures(BaseModel):
    square_footage: float = Field(..., example=1550.0)
    bedrooms: int = Field(..., example=3)
    bathrooms: float = Field(..., example=2.0)
    year_built: int = Field(..., example=1997)
    lot_size: float = Field(..., example=6800.0)
    distance_to_city_center: float = Field(..., example=4.1)
    school_rating: float = Field(..., example=7.6)

class PredictionRequest(BaseModel):
    houses: List[HouseFeatures]

@app.get("/health")
def health_check():
    if not model_artifact:
        raise HTTPException(status_code=503, detail="Model missing.")
    return {"status": "healthy"}

@app.get("/model-info")
def get_model_info():
    if not model_artifact:
        raise HTTPException(status_code=503, detail="Model not loaded.")
    return {
        "coefficients": dict(zip(model_artifact["features"], model_artifact["model"].coef_)),
        "intercept": model_artifact["model"].intercept_,
        "metrics": model_artifact["metrics"]
    }

@app.post("/predict")
def predict_price(request: PredictionRequest):
    if not model_artifact:
        raise HTTPException(status_code=503, detail="Model not loaded.")
    
    # Convert incoming JSON payload to a DataFrame
    df = pd.DataFrame([house.model_dump() for house in request.houses])
    
    # Ensure column order matches training data
    df = df[model_artifact["features"]]
    
    # Make prediction
    predictions = model_artifact["model"].predict(df)
    return {"predictions": predictions.tolist()}