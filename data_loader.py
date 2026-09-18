import pandas as pd

def load_tickets(path="support_tickets.csv"):
    df = pd.read_csv(path)
    df["created_at"] = pd.to_datetime(df["created_at"])
    return df