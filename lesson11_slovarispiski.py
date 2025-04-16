beers = {
    'Маша' : ['lager', 'ris', 'sour', 'tomatOcka'],
    'Влад' : ['lager', 'ipa','gose'],
    'Женя' : ['lager','stout',
              'neipa'
              ]
}
for name, beer in beers.items():
    print(f"\n {name} , любит пиво:")
    for pivo in beer:
        print(pivo)

