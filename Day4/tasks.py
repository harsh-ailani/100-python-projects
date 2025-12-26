# Randomization
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_number_0_to_10 = random.random() * 10
print(random_number_0_to_10)

random_float = random.uniform(0, 10)
print(random_float)

# Heads or Tails
random_number = random.randint(0, 1)
print(f"Random Number for heads and tails: {random_number}")
if random_number == 0:
    print("Heads")
else:
    print("Tails")


# Lists

fruits = ["apple", "orange", "banana"]
print(fruits)
print(fruits[0])

fruits.append("kiwi")
print(fruits)

fruits.extend(["jackfruit", "grapes", "coconut"])
print(fruits)

# Random choice
# 1st option
print(random.choice(fruits))

# 2nd option
print(len(fruits))
randon_index = random.randint(0, len(fruits)-1)
print(fruits[randon_index])

# List of lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])
