kal = 0
while True:
    kal += 4
    if kal > 100:
        break
    if kal % 6 == 0:
        continue
    print(kal)