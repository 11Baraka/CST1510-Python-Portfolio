# RECORD CHECK - AI / Data Science
# Name: Baraka
# Lane: AI / Data Science
# Date: 26 November 2026
#
# Run it with: python template_solved_W5.py
#
# Each record stores a dataset name, rows loaded and rows expected.
# The report compares the loaded rows with the expected total.

class Record:
    # Shared count of records that are OVER LIMIT.
    over_limit_count = 0

    def __init__(self, label, value, limit):
        # Store the dataset label, rows loaded and rows expected.
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        # Return OVER LIMIT, WARNING or OK for this dataset.
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    # Read label,value,limit lines and return a list of Record objects.
    records = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                label, value, limit = line.strip().split(",")
                records.append(Record(label, float(value), float(limit)))

    return records


records = load_records("records_sample.txt")

# Print one report for each dataset.
for record in records:
    status = record.status()  # Call status once per record.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"  Rows loaded   : {record.value:.0f}")
    print(f"  Rows expected : {record.limit:.0f}")
    print(f"  Status        : {status}")
    print("=" * 34)

print()
print(f"Total OVER LIMIT: {Record.over_limit_count} of {len(records)} records")
