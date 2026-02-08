from datetime import datetime, timedelta
import re
import json

print("This program choose users for greeting.");

DEFAULT_GREETING_PERIOD_DAYS = 7

# This function was described in TASK 1. 
# We need to rebuild it a little to return positive value in date in the future for confortable work
# We need to rebuilt it to organise code as module for import in TASK 4
# This is only a copy and will be delete from task 4 in the future
def get_days_from_today(date: datetime | str) -> int | None:
    today = datetime.now().date()
    try:
        if isinstance(date, str):
            # accept YYYY-MM-DD or YYYY.MM.DD
            if re.match(r"^\d{4}[.-]\d{2}[.-]\d{2}$", date):
                fmt = "%Y-%m-%d" if "-" in date else "%Y.%m.%d"
                date = datetime.strptime(date, fmt).date()
            else:
                print("Invalid date format. Please enter the date in YYYY-MM-DD or YYYY.MM.DD format")
                return None
        delta = date - today
        return delta.days
    except ValueError as e:
        print(f"Invalid date format: {date} could not be used as date.")
        return None

    
# Return all users for greeting with congratulation_date
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    result = []
    current_year = datetime.now().year
    for user in users:
        upcomming_birthday = str(current_year) + user.get("birthday")[4:]
        upcoming_birthday_days = get_days_from_today(upcomming_birthday)
        if upcoming_birthday_days < 0:
          upcomming_birthday = str(current_year + 1) + user.get("birthday")[4:]
          upcoming_birthday_days = get_days_from_today(upcomming_birthday)

        if 0 <= upcoming_birthday_days < DEFAULT_GREETING_PERIOD_DAYS:
            selebrateDay = datetime.strptime(upcomming_birthday, "%Y.%m.%d").date()
            
            if selebrateDay.weekday() == 5: # Saturday
                upcomming_birthday = (selebrateDay + timedelta(days=2)).strftime("%Y.%m.%d")
            elif selebrateDay.weekday() == 6: # Sunday
                upcomming_birthday = (selebrateDay + timedelta(days=1)).strftime("%Y.%m.%d")

            result.append({
                "name": user.get("name"),
                "birthday": user.get("birthday"),
                "congratulation_date": upcomming_birthday
            })        

    result.sort(key=lambda x: x["congratulation_date"])
    return result

users = [{
    "name": "Alice",
    "birthday": "1990.02.08"
}, {
    "name": "Bob",
    "birthday": "1985.02.09"
}, {
    "name": "Charlie",
    "birthday": "2000.02.11"
}, {
    "name": "David",
    "birthday": "1995.02.10"
}, {
    "name": "Eve",
    "birthday": "1992.02.14"
}, {
    "name": "Frank",
    "birthday": "1988.02.15"
}, {
    "name": "Grace",
    "birthday": "1993.09.18"
}, {
    "name": "Heidi",
    "birthday": "1991.02.28"
}, {
    "name": "Ivan",
    "birthday": "1987.06.12"
}, {
    "name": "Judy",
    "birthday": "1994.04.22"
}, {
    "name": "Karl",
    "birthday": "1989.08.05"
}, {
    "name": "Leo",
    "birthday": "1996.10.30"
}, {
    "name": "Mallory",
    "birthday": "1990.12.01"
}, {
    "name": "Nina",
    "birthday": "1992.01.15"
}]
    
greetings = get_upcoming_birthdays(users)

print(f"Upcoming birthdays:\n{json.dumps(greetings, indent=2, default=str)}")