n = int(input())
x = int(input())
a = list(map(int, input().split()))
b = [0]*(n+1)
b[0] = 1
if n > 1:
    b[1] = 1
if 1 in a:
    b[1] = 0

for i in range(2, n+1):
    if i in a:
        b[i] = 0
    else:
        b[i] = b[i-1] + b[i-2]

print(b[n])
