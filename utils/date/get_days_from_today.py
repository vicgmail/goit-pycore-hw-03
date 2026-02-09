from datetime import datetime
import re


"""
Calculates the number of days from today to a given date
Input date format: string "YYYY-MM-DD" or datetime object
"""
def get_days_from_today(date: datetime | str) -> int | None:
    today = datetime.now().date()
    print(f"Today's date: {today.strftime('%Y-%m-%d')}")
    try:
        if isinstance(date, str):
            if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                date = datetime.strptime(date, "%Y-%m-%d").date()
            else:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format")
                return None
        delta = today - date
        return delta.days
    except ValueError as e:
        print(f"Invalid date format: {date} could not be used as date.")
        return None 


def main():
    date_input = input("Enter a date (YYYY-MM-DD): ")    
    days = get_days_from_today(date_input)
    if days is not None:
        print(f"Result: {int(days)} days from today to {date_input}")


if __name__ == "__main__":
    main()