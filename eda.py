import pandas as pd
import numpy as np

# Load clean flattened data
df = pd.read_csv("data/processed/sample_5000_clean.csv")

print("Shape:", df.shape)

# ======================================================================
# Identify provider (non-drug) columns
# ======================================================================
provider_cols = [
    "npi", "settlement_type", "generic_rx_count",
    "specialty", "years_practicing", "gender",
    "region", "brand_name_rx_count"
]

# Identify drug columns → everything except provider columns
drug_cols = [c for c in df.columns if c not in provider_cols]

print("Number of drug columns:", len(drug_cols))

# ======================================================================
# 1. TOTAL PRESCRIPTIONS
# ======================================================================
df["total_prescriptions"] = df[drug_cols].sum(axis=1)
print(df["total_prescriptions"].describe())

# ======================================================================
# 2. BRAND SHARE
# ======================================================================
df["brand_share"] = df["brand_name_rx_count"] / df["total_prescriptions"]
df["brand_share"] = df["brand_share"].fillna(0)

# ======================================================================
# 3. GENERIC SHARE
# ======================================================================
df["generic_share"] = df["generic_rx_count"] / df["total_prescriptions"]
df["generic_share"] = df["generic_share"].fillna(0)

# ======================================================================
# 4. RX PER YEAR
# ======================================================================
df["rx_per_year"] = df["total_prescriptions"] / df["years_practicing"]
df["rx_per_year"].replace([np.inf, -np.inf], 0, inplace=True)

print(df["rx_per_year"].describe())

# ======================================================================
# 5. VALUE SCORE (weighted KPI)
# ======================================================================
df["value_score"] = (
      (df["total_prescriptions"] / df["total_prescriptions"].max()) * 0.6
    + df["brand_share"] * 0.3
    + (df["rx_per_year"] / df["rx_per_year"].max()) * 0.1
)

print(df["value_score"].describe())

# ======================================================================
# 6. SEGMENTATION (Low / Medium / High)
# ======================================================================
df["segment"] = pd.qcut(
    df["value_score"], 
    q=3, 
    labels=["Low", "Medium", "High"]
)

print("\nSegment counts:")
print(df["segment"].value_counts())

# ======================================================================
# CREATE FINAL DOCTOR KPI TABLE
# Keep ONLY KPIs → remove all drug columns completely
# ======================================================================

kpi_df = df[[
    "npi",
    "settlement_type",
    "specialty",
    "years_practicing",
    "gender",
    "region",
    "generic_rx_count",
    "brand_name_rx_count",
    "total_prescriptions",
    "brand_share",
    "generic_share",
    "rx_per_year",
    "value_score",
    "segment"
]]

# Save final output
kpi_df.to_csv("data/processed/doctor_kpis.csv", index=False)
print("\nSaved CLEAN doctor_kpis.csv with shape:", kpi_df.shape)
