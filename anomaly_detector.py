import pandas as pd

def find_anomalies(df):
    now = pd.Timestamp.now()
    hours_open = (now - df["created_at"]).dt.total_seconds() / 3600
    stuck_tickets = df[
        (df["status"].isin(["Open", "Escalated"])) &
        (df["priority"].isin(["High", "Critical"])) &
        (hours_open > 24)
    ]
        
    avg_resolution = df["resolution_time_hrs"].mean()
    slow_tickets = df[df["resolution_time_hrs"] > (2 * avg_resolution)]

    return stuck_tickets, slow_tickets