import random
import pandas as pd
from datetime import datetime

def generate_sensor_data(product_id="REV-001"):
    data = {
        "product_id": product_id,
        "temperature": random.randint(20, 45),
        "vibration": random.choice([0, 1]),
        "usage_cycles": random.randint(1, 120),
        "carbon_score": round(random.uniform(1.5, 5.0), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return data

def generate_lifecycle_log(rows=10):
    records = []
    for _ in range(rows):
        records.append(generate_sensor_data())
    return pd.DataFrame(records)

if __name__ == "__main__":
    df = generate_lifecycle_log()
    df.to_csv("sample_data.csv", index=False)
    print("Sample lifecycle data generated.")
