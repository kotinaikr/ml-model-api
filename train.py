import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def train_and_save_model():
    # Load the dataset that contains the 'price' target variable
    df = pd.read_csv('TestDataForPrediction.csv')

    # Define the exact features we want the model to use
    feature_columns = [
        'square_footage', 'bedrooms', 'bathrooms', 'year_built', 
        'lot_size', 'distance_to_city_center', 'school_rating'
    ]
    
    X = df[feature_columns]
    y = df['price']

    # Train the Linear Regression Model
    model = LinearRegression()
    model.fit(X, y)

    # Calculate metrics to return in our /model-info endpoint later
    predictions = model.predict(X)
    metrics = {
        "mse": float(mean_squared_error(y, predictions)),
        "r2_score": float(r2_score(y, predictions))
    }

    # Package the model, metrics, and feature list into one object
    model_artifact = {
        "model": model,
        "metrics": metrics,
        "features": feature_columns
    }
    
    # Save the artifact to disk
    joblib.dump(model_artifact, "model.joblib")
    print("Model trained and saved to model.joblib successfully!")

if __name__ == "__main__":
    train_and_save_model()