import random

num = random.randint(1, 43,)
print(f"Случайное нечетное число от 1 до 43: {num}")

if num == 15:
    print('Поздравляю, вы выиграли')
if num % 2== 0:
    print('Четные числа в лотерее не участвуют')
else:
    print("Чмо, проиграло")
