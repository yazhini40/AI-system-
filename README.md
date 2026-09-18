# AI Support Ticket Assistant

An AI-powered system for analyzing support tickets that answers natural language questions about ticket data and flags anomalies.

## Setup

1. Clone this repository

2. Install dependencies:pip install -r requirement.txt

3. Create a `.env` file in the project root with your free Groq API key: GROQ_API_KEY
(Get a free key at https://console.groq.com/keys)

4. Run the app:
streamlit run streamlit_app.py

5. Open the link Streamlit gives you in your browser

## Architecture

- `data_loader.py` — loads and prepares the support ticket CSV data
- `anomaly_detector.py` — rule-based logic that flags:
- High/Critical priority tickets that have been open for more than 24 hours
- Tickets with resolution times more than double the average
- `llm_query.py` — takes a natural language question, sends it to an LLM (via Groq, using the `openai/gpt-oss-120b` model, free tier), which generates a line of pandas code to answer it; that code is then executed against the data
- `streamlit_app.py` — the web interface tying everything together: a text box for questions, and a button to view anomalies

## Tools used

- **Python** with **pandas** for data handling
- **Groq API** (free tier) with the `openai/gpt-oss-120b` model for natural language understanding
- **Streamlit** for the web interface

## Example questions

- "How many tickets are currently open?"
- "How many tickets have high priority?"
- "What is the average resolution time?"

## Limitations

- The LLM is explicitly told the exact valid values for `priority` and `status` columns in the prompt, since without this it sometimes guessed incorrect wording (e.g. "high priority" instead of "High") and returned wrong answers.
- Uses `eval()` to run LLM-generated code, which would need sandboxing/validation for production use.
- Anomaly thresholds (24 hours, 2x average) are simple fixed rules rather than statistically tuned thresholds.