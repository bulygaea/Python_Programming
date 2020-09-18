def C(n, k):
    if k == n or k == 0:
        return 1
    if k != 1:
        return C(n-1, k-1) + C(n-1, k)
    else:
        return n


a = int(input())
b = int(input())
print(C(a, b))
