def deg(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return deg(a*a, n//2)
    else:
        return a * deg(a, n-1)


a = float(input())
n = float(input())
print(deg(a, n))
