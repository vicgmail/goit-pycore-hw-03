import random


#Return a list of randomly selected unique numbers
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min >= max or quantity <= 0 or quantity > max - min + 1:
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


def main():
    try:
        min_input = int(input("Enter the minimum number: "))
        max_input = int(input("Enter the maximum number: "))
        quantity_input = int(input("Enter the quantity of numbers to generate: "))

        result = get_numbers_ticket(min_input, max_input, quantity_input)
        print(f"Generated numbers: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers for minimum, maximum, and quantity.")


if __name__ == "__main__":
    main()