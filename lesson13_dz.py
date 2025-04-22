def name(first_name="",second_name="", last_name=""):
    while True:
        fio1 = str(input(f'Имя:{first_name}'))
        fio2 = str(input(f'Отчество:{second_name}'))
        fio3 = str(input(f'Фамилия:{last_name}'))

        if not fio3:
            raise ValueError("Пошёл нахуй")
        if fio2:
            full_name = f'{fio1} {fio2} {fio3}'
            print(full_name.title())
        else:
            full_name = f'{fio1} {fio3}'
            print(full_name.title())
try:
    FIO = name()
    print(FIO)
except ValueError as error:
    print(error)