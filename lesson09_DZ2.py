beer_prices = {
    'lager': 150,
    'ris': 250,
    'sour': 180,
    'tomatOcka': 120
}

print("У нас есть такие сорта пива:")
for beer in beer_prices.keys():
    print("-", beer)
print("Пиво дешевле 200 рублей:")
for name, price in beer_prices.items():
    if price < 200:
        print(f"- {name}: {price} руб.")