"""
RECORD CHECK - AI / Data Science lane
Name: ____________________
Lane: AI / Data Science
Date: ____________________

Run it with: python template.py
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean one messy survey record and return it as a dictionary."""
    line = raw_line.strip()
    parts = line.split(",")
    survey_name = parts[0].strip().lower()

    fields = {}
    for piece in parts[1:]:
        key, value = piece.split("=", 1)
        fields[key.strip().lower()] = value.strip()

    return {
        "survey": survey_name,
        "rating": float(fields["rating"]),
        "age": int(fields["age"])
    }


def status_of(rating):
    """Flag ratings below 3; treat ratings of 3 or above as OK."""
    if rating < 3:
        return "FLAGGED"
    return "OK"


# ====================================================================== INPUT
# Deliberately inconsistent spacing and case to practise cleaning.
raw_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "CUSTOMER_PULSE,rating=2,age=31",
    "  Student_Feedback , RATING = 5 , AGE = 19 ",
    "health_survey, rating=3, age=42",
    "  PRODUCT_TEST , rating=1 , age=27 "
]

# Excellent: save raw records to a file, then load them from the file.
input_path = "survey_records.txt"
with open(input_path, "w", encoding="utf-8") as file:
    for raw_record in raw_records:
        file.write(raw_record + "\n")

with open(input_path, "r", encoding="utf-8") as file:
    raw_records = [line.rstrip("\n") for line in file]


# =============================================================== PROCESS + OUTPUT
flagged_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record["rating"])
        print(record, "|", status)
        if status == "FLAGGED":
            flagged_count += 1
    except (ValueError, KeyError) as error:
        print("Could not parse:", raw_record, "|", error)

print(f"Summary: {len(raw_records)} records, {flagged_count} flagged.")


# =================================================================== ERROR TEST
# This deliberately invalid value demonstrates ValueError from float().
bad_record = "broken_survey, rating=high, age=22"
try:
    print(parse_line(bad_record))
except ValueError as error:
    print("Expected conversion error:", error)
