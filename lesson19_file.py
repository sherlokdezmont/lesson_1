exit1 = 'quit'
while True:
    x = input('Введите первое число:')
    if x == exit1:
        break
    y = input('Введите второе число:')
    if y == exit1:
        break
    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
            print('u cant divide by zero')
    else:
        print(result)
