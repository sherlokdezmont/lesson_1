nalogi = ["vlozheniya", "vichitaniya", "investicii", "baldezh", "zhopa"]
for nalog in nalogi:
    if nalog != 'zhopa':
        print(nalog.lower())
    else:
        print(nalog.title())