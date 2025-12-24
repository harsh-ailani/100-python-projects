# Task1 - Conditionals
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can go on the ride !")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif 12 <= age <= 18:
        bill = 7
        print("Youth ticket is $7")
    else:
        bill = 12
        print("Adult ticket is $12")

    wants_photo = input("Do you want a photo? - Y or N : ")
    if wants_photo == "Y":
        # Add photo amount $3 to the total bill
        bill += 3

    print(f"Your total bill is: ${bill}")
else:
    print("You can not enter")

# Task2 - Modulo operator
number = int(input("What is the number you want to check? "))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

# Task3 - Pizza bill calculator
print("Welcome to Python Pizza Delivery")
bill = 0

size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid input.")

if size in ["S", "M", "L"]:  # Proceed only if the size input was valid
    if input("Do you want pepperoni? Y or N: ") == "Y":
        bill += 2 if size == "S" else 3

    if input("Do you want extra cheese? Y or N: ") == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}")

