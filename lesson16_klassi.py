class Beer:
    def __init__(self, beer_name):
        self.name = beer_name
    def beers(self):
        return f'Какое классное пиво, {self.name}'

pivo = Beer("лагер")
print(pivo.beers())

class Menu:
    def __init__(bludo, dnya):
        bludo.name = dnya
    def bludo_dnya(bludo):
        return f'Сегодня, блюдо дня: {bludo.name}'

eda = Menu("Спаггети")
print(eda.bludo_dnya())