def gen(m):
    s = 1
    for i in range(1, m):
        yield i**2 + s
        s+=1

a = gen(5)
for i in a:
    print(i)
