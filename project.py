import json
import pandas as pd

# STEP 1: Load only a SAMPLE from the big JSONL to avoid memory issues
file_path = "data/raw/data.jsonl"

data_list = []
max_rows = 5000  # small sample so your laptop is safe

with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= max_rows:
            break
        data_list.append(json.loads(line))

df = pd.DataFrame(data_list)

print("Loaded shape:", df.shape)
print(df.head())

# Save this sample as a CSV so we don't keep touching the big JSONL
output_path = "data/processed/sample_5000_raw.csv"
df.to_csv(output_path, index=False)
print("Saved sample to:", output_path)
