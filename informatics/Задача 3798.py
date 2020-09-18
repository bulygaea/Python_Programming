def IsPrime(n):
    b = 2
    while b*b <= n and n % b != 0:
        b += 1
    return b*b > n


a = int(input())
if IsPrime(a):
    print('YES')
else:
    print('NO')
