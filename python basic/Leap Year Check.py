#Leap Year Check in Python

print("Leap Year Checker")

while True:
    # 1. Ask the user for a year and convert it to an integer (number)
    year = int(input("Enter a year to check: "))

    # 2. Check the leap year rules using if/elif/else
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # divisible by 4 or 400 means leap year
        print(f"Yes, {year} is a leap year! ")

    else:                            
        print(f"No, {year} is NOT a leap year.")