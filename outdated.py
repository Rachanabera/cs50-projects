months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    try:
        date = input("Date: ").strip()

        # Format: MM/DD/YYYY
        if "/" in date:
            parts = date.split("/")
            if len(parts) == 3:
                month, day, year = parts
                month, day = int(month), int(day)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{int(year):04}-{month:02}-{day:02}")
                    break

        # Format: Month Day, Year
        elif "," in date:
            parts = date.split()
            if len(parts) == 3:
                month_name, day, year = parts
                day = day.replace(",", "")
                if month_name in months and 1 <= int(day) <= 31:
                    print(f"{int(year):04}-{months[month_name]}-{int(day):02}")
                    break

    except (ValueError, IndexError):
        pass
