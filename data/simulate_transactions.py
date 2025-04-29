import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

# Static Data for Simulation
locations = ["New York, USA", "Los Angeles, USA", "London, UK", "Paris, France", "Mumbai, India"]
devices = ["iphone14-pro-max", "samsung-s23", "ipad-pro", "macbook-air", "pixel-6"]

# Create random users
def generate_user_ids(n):
    return [f"user_{uuid.uuid4().hex[:8]}" for _ in range(n)]

# Generate a single transaction
def generate_transaction(user_id):
    timestamp = datetime.now() - timedelta(minutes=random.randint(0, 10000))
    amount = round(random.uniform(5, 5000), 2)  # between $5 and $5000
    location = random.choice(locations)
    device = random.choice(devices)
    typing_speed = random.uniform(30, 80)  # words per minute
    touch_pressure = random.uniform(0.5, 1.5)  # arbitrary units
    return {
        "user_id": user_id,
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "transaction_amount": amount,
        "location": location,
        "device_id": device,
        "typing_speed": round(typing_speed, 2),
        "touch_pressure": round(touch_pressure, 2)
    }

# Main function to simulate a dataset
def simulate_transactions(num_users=50, transactions_per_user=20):
    data = []
    user_ids = generate_user_ids(num_users)
    
    for user in user_ids:
        for _ in range(transactions_per_user):
            txn = generate_transaction(user)
            data.append(txn)
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = simulate_transactions()
    df.to_csv("transactions.csv", index=False)
    print("✅ Transaction data generated: transactions.csv")
