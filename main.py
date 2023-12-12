a = 10000
c = 0
while a < 1555555666:
    b = a % 3
    bin(a)
    bin(b)
    a *= 4
    a += b
    c = a % 5
    if c < 4:
        a *= 4
        a += c
    else:
        a *= 8
        a += c
    if (a >= 1222222222) and (a <= 1555555666):
        c += 1
    a += 1

print(c)