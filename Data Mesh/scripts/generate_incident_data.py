import pandas as pd
import random
from faker import Faker

fake = Faker()

incidents = []

for i in range(200):
    incidents.append({
        "incident_id": i + 1,
        "severity": random.choice(["P1", "P2", "P3"]),
        "system": random.choice([
            "Trade Engine",
            "Payment Gateway",
            "Reconciliation",
            "API Gateway"
        ]),
        "status": random.choice(["OPEN", "RESOLVED"]),
        "sla_breach": random.choice(["YES", "NO"]),
        "timestamp": fake.date_time_between(start_date="-7d", end_date="now")
    })

df = pd.DataFrame(incidents)

df.to_csv("data/incident_data.csv", index=False)

print("Incident data generated.")