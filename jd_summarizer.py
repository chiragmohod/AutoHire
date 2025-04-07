import pandas as pd
import ollama
from tqdm import tqdm
import os

# File paths
input_csv = "D:\hackathon\data\job_description.csv"
output_csv = "summarized_jobs.csv"

# Load job descriptions
df = pd.read_csv(input_csv, encoding='ISO-8859-1')

# Function to summarize JD
def summarize_jd(description):
    prompt = (
        "Summarize the following job description into clear bullet points for:\n"
        "- Required Skills\n- Experience\n- Education\n- Responsibilities\n\n"
        f"{description}"
    )
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        print(f"❌ Error during summarization: {e}")
        return "Error summarizing this JD"

# Apply summarization
tqdm.pandas(desc="Summarizing JDs")
df["JD_Summary"] = df["Job Description"].progress_apply(summarize_jd)

# Save the new file
df.to_csv(output_csv, index=False, encoding='utf-8')
print(f"✅ All summaries saved to {output_csv}")
