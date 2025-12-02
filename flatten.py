import pandas as pd
import json

# -------------------------
# STEP 2: Load 5000-sample CSV
# -------------------------
df = pd.read_csv("data/processed/sample_5000_raw.csv")
print("Loaded sample shape:", df.shape)

# -------------------------
# Flatten provider_variables
# -------------------------
def safe_json(x):
    try:
        return json.loads(x.replace("'", '"'))
    except:
        return {}

provider_expanded = df['provider_variables'].apply(safe_json)
provider_df = pd.json_normalize(provider_expanded)
print("Provider DF:", provider_df.shape)

# -------------------------
# Flatten cms_prescription_counts
# -------------------------
presc_expanded = df['cms_prescription_counts'].apply(safe_json)
presc_df = pd.json_normalize(presc_expanded)
print("Prescription DF:", presc_df.shape)

# -------------------------
# Combine final table
# -------------------------
final_df = pd.concat([df[['npi']], provider_df, presc_df], axis=1)
print("Combined DF:", final_df.shape)

# -------------------------
# Save clean file
# -------------------------
final_df.to_csv("data/processed/sample_5000_clean.csv", index=False)
print("Saved: data/processed/sample_5000_clean.csv")
