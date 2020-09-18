def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


a = float(input())
b = float(input())
if IsPointInSquare(a, b):
    print('YES')
else:
    print('NO')
