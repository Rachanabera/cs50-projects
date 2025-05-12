import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regular expression pattern to match the given time formats
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.match(pattern, s.strip())

    if not match:
        raise ValueError("Invalid time format")

    # Extract values from the regex match
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    # Convert hours and minutes to integers
    hour1 = int(hour1)
    hour2 = int(hour2)
    minute1 = int(minute1) if minute1 else 0
    minute2 = int(minute2) if minute2 else 0

    # Validate minutes (should be between 00 and 59)
    if not (0 <= minute1 <= 59) or not (0 <= minute2 <= 59):
        raise ValueError("Invalid minute value")

    # Convert the first time (start time) to 24-hour format
    if period1 == "AM":
        if hour1 == 12:  # 12 AM is midnight
            hour1 = 0
    elif period1 == "PM":
        if hour1 != 12:  # 12 PM is noon
            hour1 += 12

    # Convert the second time (end time) to 24-hour format
    if period2 == "AM":
        if hour2 == 12:  # 12 AM is midnight
            hour2 = 0
    elif period2 == "PM":
        if hour2 != 12:  # 12 PM is noon
            hour2 += 12

    # Format the times as 24-hour times
    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()
