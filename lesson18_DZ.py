import random

number = random.randint(1, 100)
print(f"Случайное число от 1 до 100: {number}")

import random

names = ["Аня", "Борис", "Вика", "Гоша"]
chosen = random.choice(names)
print(f"Случайно выбранный человек: {chosen}")

def get_user_name():
    return "Аня"

class MyClass:
    pass

MAX_COUNT = 100

