import random

numbers = range(7)

for i in numbers:
    print(random.choice(numbers))
    next = input("Do You Want To Continue? (y/n): ")
    if next.lower() != "y":
        break

