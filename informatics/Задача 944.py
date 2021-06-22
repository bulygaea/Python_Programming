n, m = map(int, input().split())
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

a = []
for i in range(n):
    a.append([0]*m)

ans = []
for i in range(n):
    ans.append(['']*m)

a[0][0] = b[0][0]
for i in range(1, m):
    a[0][i] = a[0][i-1] + b[0][i]
    ans[0][i] = ans[0][i-1] + ' R'

for i in range(1, n):
    a[i][0] = a[i-1][0] + b[i][0]
    ans[i][0] = ans[i-1][0] + ' D'

for i in range(1, n):
    for j in range(1, m):
        if a[i-1][j] > a[i][j-1]:
            a[i][j] = a[i-1][j] + b[i][j]
            ans[i][j] = ans[i-1][j] + ' D'
        else:
            a[i][j] = a[i][j-1] + b[i][j]
            ans[i][j] = ans[i][j-1] + ' R'

print(a[n-1][m-1])
print(ans[n-1][m-1])
