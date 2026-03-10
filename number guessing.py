import random

start = 1
end = 100
tries = 0
secret = random.randint(start, end)
number = 0
print(f"Enter a number between {start} and {end}")
while True:
    number = int(input("Enter a number: "))
    if number < secret and number >= start and number <= end:
        print("Ur number is too low")
        tries += 1
        print(f"tries count: {tries}")
        continue
    elif number > secret and number >= start and number <= end:
        print("Ur number is too high")
        tries += 1
        print(f"tries count: {tries}")
        continue
    elif number == secret:
        print("You won")
        print(f"It took you {tries} tries")
        break
    else:
        print(f"Enter a number between {start} and {end}")
        continue

