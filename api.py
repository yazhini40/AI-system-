from fastapi import FastAPI
from pydantic import BaseModel
from data_loader import load_tickets
from anomaly_detector import find_anomalies
from llm_query import ask_question

app = FastAPI()
df = load_tickets()

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query(request: QueryRequest):
    answer = ask_question(request.question, df)
    return {"question": request.question, "answer": str(answer)}

@app.get("/anomalies")
def anomalies():
    stuck, slow = find_anomalies(df)
    return {
        "stuck_high_priority_tickets": stuck[["ticket_id", "priority", "status"]].to_dict(orient="records"),
        "slow_resolutions": slow[["ticket_id", "resolution_time_hrs"]].to_dict(orient="records")
    }