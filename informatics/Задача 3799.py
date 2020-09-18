def MinDivisor(n):
    b = 2
    while b*b <= n and n % b != 0:
        b += 1
    if n % b == 0:
        return b
    else:
        return n


a = int(input())
print(MinDivisor(a))
