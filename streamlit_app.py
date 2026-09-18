import streamlit as st
from data_loader import load_tickets
from anomaly_detector import find_anomalies
from llm_query import ask_question

st.title("Support Ticket Assistant")

df = load_tickets()
st.write(f"Loaded {len(df)} tickets")

st.header("Ask a question")
question = st.text_input("Type your question about the tickets:")
if question:
    answer = ask_question(question, df)
    st.write("**Answer:**", answer)

st.header("Anomalies")
if st.button("Check for anomalies"):
    stuck, slow = find_anomalies(df)
    st.subheader(f"Stuck high-priority tickets ({len(stuck)})")
    st.dataframe(stuck[["ticket_id", "priority", "status", "created_at"]])
    st.subheader(f"Unusually slow resolutions ({len(slow)})")
    st.dataframe(slow[["ticket_id", "resolution_time_hrs"]])