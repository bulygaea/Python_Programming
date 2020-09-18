def clean(n):
    if n == 1:
        return [-1]
    elif n == 2:
        return [-2, -1]
    else:
        return clean(n - 2) + [-n] + fill(n - 2) + clean(n - 1)


def fill(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        return fill(n - 1) + clean(n - 2) + [n] + fill(n - 2)


x = int(input())
print(*fill(x))
