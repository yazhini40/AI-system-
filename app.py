from data_loader import load_tickets
from anomaly_detector import find_anomalies

df = load_tickets()
print("Loaded", len(df), "tickets")

stuck, slow = find_anomalies(df)
print("Stuck high-priority tickets:", len(stuck))
print(stuck[["ticket_id", "priority", "status", "created_at"]])

print("\nUnusually slow resolutions:", len(slow))
print(slow[["ticket_id", "resolution_time_hrs"]])

from llm_query import ask_question

answer = ask_question("How many tickets are currently open?", df)
print("\nLLM Answer:", answer)