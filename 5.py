import random

while True:
    a = int(input("Your a is: "))

    if (a > 200 or a < 0):
        print("estebahe 0 namishe bashe")
    else:
        break

numbers = random.sample(range(0, 200), a)
print(numbers)

