# Physician Segmentation & Sales Optimization (Pharma Analytics Project)

# Objective
This project simulates a real ZS Associates Decision Analytics workflow, focusing on converting raw healthcare data into doctor-level insights that support sales force optimization.

1️. Dataset Overview

The original dataset contained 239,930 JSONL records, each with two nested objects:

A. provider_variables (doctor-level attributes): specialty, region, gender, settlement_type, years_practicing, brand_name_rx_count, generic_rx_count

B. cms_prescription_counts (drug-level prescriptions): drug_name : number_of_prescriptions

Because the dataset was extremely large, a 5,000-row sample was used for analysis.

2️. Data Processing Pipeline
✔ Step 1 — Sample Extraction

Extracted 5,000 JSONL records for memory efficiency.
📁 Output: data/processed/sample_5000_raw.csv

✔ Step 2 — Flattening Nested JSON - Converted nested structures into a flat table : 7 doctor attributes, 1,415 drug columns

📁 Output: data/processed/sample_5000_clean.csv

✔ Step 3 — KPI Creation - Derived 6 core business KPIs, typically used in pharma analytics:

total_prescriptions- Total prescriptions written by a doctor across all drugs.
brand_share- % of prescriptions from the focal brand.
generic_share- % of prescriptions that are generic drugs.
rx_per_year- Prescriptions normalized by years practicing.
value_score (ZS-style scoring)- Composite score using: 60% → total_prescriptions (scaled), 30% → brand_share and10% → rx_per_year (scaled)

segment - Labels doctors as High / Medium / Low using quantiles.

📁 Output: data/processed/doctor_kpis.csv

3️. Business Insights (Consulting Style)
🔹 1. Doctor Segmentation:
              High-value doctors generate 5–7× more prescriptions.
              Low segment dominated by general practitioners.
              Recommendation: Increase engagement & visit frequency for High segment.

🔹 2. Brand Share:
             Several doctors have 0% brand share, showing weak loyalty.
             Specialists (Cardiology, Nephrology) show naturally higher affinity.
             Recommendation: Improve brand messaging & sampling programs.

🔹 3. Region Performance:
              South & Midwest show strong volume.
              West has lower volume but more specialists.
              Recommendation: Reallocate reps toward high-performing regions.

🔹 4. Specialty Behavior: 
              Specialists have significantly higher value scores.
              GPs have lower Rx volume & generic-heavy patterns.
              Recommendation: Prioritize specialist-targeted promotions.

4️. Dashboard Summary (Power BI):

Dashboard includes: Doctor count by segment, Average prescriptions by segment, Brand share distribution, Generic vs brand share, Prescriptions by specialty, KPI cards- Total Doctors, Avg. Total Prescriptions, Avg. Value Score


5️. Tech Stack: Python (pandas, json), Power BI (visualization), CSV / JSONL (data storage)
