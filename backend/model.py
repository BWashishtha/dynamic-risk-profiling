import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load simulated transaction data
def load_data():
    df = pd.read_csv("../data/transactions.csv")
    return df

# Feature Engineering
def preprocess(df):
    # Convert timestamp to numerical features (Hour of Day)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    
    features = [
        "transaction_amount",
        "typing_speed",
        "touch_pressure",
        "hour"
    ]
    
    X = df[features]
    return X

# Train Isolation Forest Model
def train_model(X):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,  # Assume 5% anomalies
        random_state=42
    )
    model.fit(X)
    return model

# Save model
def save_model(model, path="risk_model.pkl"):
    joblib.dump(model, path)
    print("✅ Model saved successfully.")

if __name__ == "__main__":
    df = load_data()
    X = preprocess(df)
    model = train_model(X)
    save_model(model)
