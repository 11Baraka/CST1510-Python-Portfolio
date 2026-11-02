# RECORD CHECK - AI / Data Science
# Name: Baraka
# Lane: AI / Data Science
# Date: 2 November 2026
#
# Run it with: python template_W04_solved.py
# Keep records_sample_week4.txt in the same folder.

# FUNCTIONS
def check_record(value, limit):
    # Calculate the remaining amount, percentage and status.
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    # Print the report for one record.
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Rows loaded   : {value:>10.2f}")
    print(f"  Rows expected : {limit:>10.2f}")
    print(f"  Rows remaining: {difference:>+10.2f}")
    print(f"  Percent       : {percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)


def load_records(path):
    # Read comma-separated lines and return a list of dictionaries.
    records = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })

    return records


# Load records safely from the data file.
try:
    records = load_records("records_sample_week4.txt")
except FileNotFoundError:
    print("records_sample_week4.txt not found. No records were loaded.")
    records = []

# Process each record, print its report and save its result.
over_limit_count = 0

with open("results_week4.txt", "w", encoding="utf-8") as results_file:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        print_report(
            record["label"], record["value"], record["limit"],
            difference, percent, status
        )

        results_file.write(f'{record["label"]},{status}\n')

        if status == "OVER LIMIT":
            over_limit_count += 1

# Print the total after the loop.
print()
print(f"OVER LIMIT records: {over_limit_count} of {len(records)}")

# Read the saved results file and display its contents.
print()
print("Saved results:")
with open("results_week4.txt", "r", encoding="utf-8") as results_file:
    print(results_file.read())
