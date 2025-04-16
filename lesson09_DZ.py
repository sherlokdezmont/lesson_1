beer_prices = {
    'lager': 150,
    'ris': 250,
    'sour': 180,
    'tomatOcka': 120,
    'ipa': 170,
    'gose': 190,
    'stout': 200,
    'neipa': 210
}

user_input = input("Введите название пива: ").strip().lower()

price = beer_prices.get(user_input)

if price:
    print(f"Стоимость пива '{user_input}' — {price} рублей.")
else:
    print(f"Пива с названием '{user_input}' нет в базе.")