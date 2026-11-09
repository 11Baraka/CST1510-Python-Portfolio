"""
RECORD CHECK — Week 6 mini-project
Lane: AI / Data Science
Input: ai_records.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file.
df = pd.read_csv("ai_records.csv")

# 2. Calculate the percentage of expected rows that were loaded.
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

# Classify each dataset. The lambda is a single expression.
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# 3. Display the complete DataFrame.
print("FULL RECORD CHECK")
print(df)

# Show only records that need attention (not OK).
print("\nRECORDS NEEDING ATTENTION")
print(df[df["status"] != "OK"])

# Count records in each status group.
print("\nCOUNTS BY STATUS")
print(df.groupby("status").size())

# Save the full report.
df.to_csv("ai_records_report.csv", index=False)
print("\nSaved ai_records_report.csv")

# Save a bar chart of status counts.
df["status"].value_counts().plot(kind="bar", title="AI datasets by status")
plt.xlabel("Status")
plt.ylabel("Number of datasets")
plt.tight_layout()
plt.savefig("ai_records_status_counts.png")
plt.show()
