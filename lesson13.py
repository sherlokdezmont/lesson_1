from lesson03_f import full_name


def favorite_beer(name, lovely_beer):
    print(f'Кстати, {name}, любит это пиво-{lovely_beer}')

favorite_beer("Masha", "Sour")
favorite_beer("Vlad", "Lager")

def favorite_drink(name, drink='pivo'):
    print(f'Даже {name}, любит {drink}')

favorite_drink("Masha")
favorite_drink("Женя")

def pivo(pivo_name, abv, ibu):
    about_pivo = f'А кстати, {pivo_name}, классное, а характеристики следующие:{abv}, {ibu}'
    return about_pivo.title()
result = pivo('lager', 5.5, 0.5)
print(result)


def name(first_name,second_name, last_name=''):
    if last_name:
        full_name = f'{first_name} {second_name} {last_name}'
    else:
        full_name = f'{first_name} {second_name}'

    return full_name.title()

FIO = name("Мальбек","Гена" )
print(FIO)

def persons(first_name, last_name):
    person = {'first_name': first_name,
              'last_name': last_name
              }
    return person
results = persons(first_name="Masha", last_name="Бальжадоровна")
print(results)


def pivas(*pivko):
    print(f'наше любимое пиво\n')
    for piv in pivko:

        print(f'-{piv}')

pivas('lager','ale','porter','lambic','stout')

