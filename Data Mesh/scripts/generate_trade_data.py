import pandas as pd
import random
from faker import Faker

fake = Faker()
rows = []

for i in range(500):
    rows.append({
        "trade_id": i + 1,
        "trade_type": random.choice(["BUY", "SELL"]),
        "amount": random.randint(1000, 50000),
        "status": random.choices(["SUCCESS", "FAILED"], weights=[85, 15])[0],
        "latency_ms": random.randint(20, 700),
        "timestamp": fake.date_time_between(start_date="-7d", end_date="now")
    })

df = pd.DataFrame(rows)
df.to_csv("data/trade_data.csv", index=False)

print("Created data/trade_data.csv")