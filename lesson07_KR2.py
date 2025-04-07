while True:
    num1 = float(input("Введите первое число:"))
    num2 = float(input("Введите второе число:"))
    if num1 < num2:
        print('Первое число меньше второго.')
    elif num1 > num2:
        print('Первое число больше второго.')
    elif num1 == num2:
        print('Первое число равно второму.')
