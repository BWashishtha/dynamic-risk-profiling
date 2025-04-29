from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

from model import preprocess  # Import your feature extraction logic

# Load the trained model
model = joblib.load("risk_model.pkl")

app = FastAPI()

# Define Request Body
class TransactionInput(BaseModel):
    transaction_amount: float
    typing_speed: float
    touch_pressure: float
    timestamp: str  # Expect ISO format (e.g., "2025-04-28 14:23:56")

@app.get("/")
async def root():
    return {"message": "Dynamic Risk Profiling API is running 🚀"}

@app.post("/evaluate")
async def evaluate_transaction(transaction: TransactionInput):
    # Convert input into DataFrame
    data = {
        "transaction_amount": [transaction.transaction_amount],
        "typing_speed": [transaction.typing_speed],
        "touch_pressure": [transaction.touch_pressure],
        "timestamp": [transaction.timestamp],
    }
    df = pd.DataFrame(data)
    
    # Feature engineering
    X = preprocess(df)
    
    # Predict anomaly
    prediction = model.decision_function(X)  # Higher = more normal, Lower = more risky
    score = -prediction[0]  # Flip to make higher = more risky
    
    # Simple risk classification
    if score > 0.75:
        risk_level = "HIGH"
    elif score > 0.5:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": round(float(score), 3),
        "risk_level": risk_level
    }
