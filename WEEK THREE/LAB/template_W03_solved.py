# RECORD CHECK - AI / Data Science
# Name: Baraka
# Lane: AI / Data Science
# Date: 15 October 2026
#
# Run it with: python template_W03_solved.py
# Type quit when you have finished entering records.

# FUNCTIONS
def status_of(percent):
    # Return the status based on the percentage.
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    # Return the difference and percentage.
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    # Print the complete report for one dataset.
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


# INPUT, PROCESS AND OUTPUT
over_limit_count = 0

while True:
    # Ask for the dataset name. Typing quit ends the loop.
    label = input("Enter dataset name (or quit to finish): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))

    # Calculate the difference and percentage using the function.
    difference, percent = check(value, limit)

    # Get the status using the percentage.
    status = status_of(percent)

    # Print the report using the report function.
    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

# Print the total once after the loop finishes.
print(f"OVER LIMIT records this session: {over_limit_count}")
