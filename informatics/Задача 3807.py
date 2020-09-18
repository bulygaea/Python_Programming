def gcd(a, b):
    if b == 0:
        print(a)
    else:
        gcd(b, a % b)


x = int(input())
y = int(input())
gcd(x, y)
