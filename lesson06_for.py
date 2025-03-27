while True:
    userinput = str(input("введите строку:"))
    kal = "аоьюеуыиАИОЭЫЕИЯя"
    count = sum(1 for char in userinput if char in kal)
    print(f"Колличество гласных букв:{count}")