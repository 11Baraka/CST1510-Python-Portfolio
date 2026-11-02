# RECORD CHECK - AI / Data Science
# Name: Baraka
# Lane: AI / Data Science
# Date: 2 November 2026
#
# Run it with: python template_W02_solved.py
#
# Enter a dataset name, rows loaded and rows expected.
# Type quit as the dataset name when you have finished.

over_limit_count = 0

while True:
    # INPUT - ask for the dataset details.
    label = input("Enter dataset name (or quit to finish): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))

    # PROCESS - calculate the difference and percentage.
    difference = limit - value
    percent = (value / limit) * 100

    # Decide which status applies.
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # OUTPUT - print the report.
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Rows loaded   : {value:>10.2f}")
    print(f"  Rows expected : {limit:>10.2f}")
    print(f"  Free          : {difference:>+10.2f}")
    print(f"  Percent       : {percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)
    print()

# Print the session total once, after the loop ends.
print(f"OVER LIMIT records this session: {over_limit_count}")
