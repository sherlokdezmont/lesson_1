def remove_duplicates(my_list):
    return list(set(my_list))

setters = {'lager',
       'ale',
       'porter',
       'lambic',
       'stout',
       'lager',
       'ale'
       }

result = remove_duplicates(setters)
setters.discard('ale')
print(setters)


