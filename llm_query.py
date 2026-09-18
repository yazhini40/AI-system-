import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_question(question, df):
    columns_info = ", ".join(df.columns.tolist())

    prompt = f"""
You are helping analyze a support tickets table with these columns: {columns_info}.
The priority column contains exactly these values: Low, Medium, High, Critical.
The status column contains exactly these values: Open, Resolved, Escalated.

Write ONE line of pandas code that answers this question about the dataframe df.
Only output the code, nothing else. The code should evaluate to the final answer.

Question: {question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    code = response.choices[0].message.content.strip()
    code = code.replace("```python", "").replace("```", "").strip()
    print("GENERATED CODE:", code)

    try:
        answer = eval(code, {"df": df, "pd": __import__("pandas")})
    except Exception as e:
        return f"Couldn't compute answer. Generated code: {code}. Error: {e}"

    return answer
