import re


COUNTRY_CODES = {
    "US": "+1",
    "UK": "+44",
    "UA": "+38",
    "DE": "+49",
    "FR": "+33"
}


#Normalizes phone numbers
def normalize_phone(phone: str, country_code: str = "+38") -> str | None:    
    digits = re.sub(r"\D+", "", phone)
    if len(digits) == 10:
        return f"{country_code}{digits}"
    elif len(digits) == 11 and country_code == COUNTRY_CODES["UA"] and digits[0] == "8":
        return f"+3{digits}"
    elif len(digits) > 10:
        return f"+{digits}"
    else:
        print(f"Invalid phone number format: {phone}")
        return None


def main():
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
        "10 111 22 11   ",
        "asd",
    ]
    sanitized_numbers = [result for num in raw_numbers if (result := normalize_phone(num)) is not None]
    print("Normalized numbers:", sanitized_numbers)


if __name__ == "__main__":
    main()
