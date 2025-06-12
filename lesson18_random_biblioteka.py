
from random import choice

beer = ["lager", "ale", "stout", "lambic", "kolsh", "baltic porter", "porter", "penis", "wild ale"]
while True:
    x = str(input('заказ пива дня'))
    if x.strip().lower() == 'одно пиво':
        beer_of_day = choice(beer)
        print(f'вот ваш {beer_of_day.title()}')
        break
    else:
        print('Иди нахуй')