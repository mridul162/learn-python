def squared_num():
    a = 1
    while True:
        yield a*a
        a += 1

for x in squared_num():
    if x>100:
        break
    print(x)