def remove_duplicates(*my_list):
    return list(set(my_list))

result = remove_duplicates('lager',
           'ale',
           'porter',
           'lambic',
           'stout',
           'lager'
           )
print(result)