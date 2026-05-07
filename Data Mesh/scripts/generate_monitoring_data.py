import pandas as pd
import random
from faker import Faker

fake = Faker()
rows = []

for i in range(300):
    api_latency = random.randint(50, 900)
    failed_requests = random.randint(0, 25)

    rows.append({
        "metric_id": i + 1,
        "system": random.choice(["Trade Engine", "API Gateway", "Reconciliation", "Payment Gateway"]),
        "cpu_percent": random.randint(20, 95),
        "memory_percent": random.randint(30, 90),
        "api_latency_ms": api_latency,
        "failed_requests": failed_requests,
        "health_status": "DEGRADED" if api_latency > 600 or failed_requests > 15 else "HEALTHY",
        "timestamp": fake.date_time_between(start_date="-7d", end_date="now")
    })

df = pd.DataFrame(rows)
df.to_csv("data/monitoring_data.csv", index=False)

print("Monitoring data generated.")