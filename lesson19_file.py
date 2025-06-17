while True:
    user_input1 = input("Введите первое число (или 'q' для выхода): ")
    if user_input1.lower() == 'q':
        print("Выход из программы.")
        break

    user_input2 = input("Введите второе число (или 'q' для выхода): ")
    if user_input2.lower() == 'q':
        print("Выход из программы.")
        break
    num1 = float(user_input1)
    if num1 == 'q':
        print("Выход из программы.")
        break
    num2 = num1 = float(user_input2)
    if num2 == 'q':
        print("Выход из программы.")
        break

    message = "Введите оператор"
    operation = input(message)
    if operation == '+':
        print('Сложение')
        result = num1 + num2
    elif operation == '-':
        print('Вычитание')
        result = num1 - num2

    elif operation == '/':
        if num2 == 0:
            try:
                result = int(num1) / int(num2)
            except ZeroDivisionError:
                print('u cant divide by zero')
        else:
            print('Деление')
            result = num1 / num2
    elif operation == '*':
        print('Умножение')
        result = num1 * num2
    else:
        print("Неизвестная операция")
        try:
            if operation != ['+', '-', '/', '*']:
                print("Неизвестная операция")
        except ZeroDivisionError:(
                    print('u cant use it'))
        print("Результат:", result)