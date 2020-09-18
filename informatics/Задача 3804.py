def summa(x, res=0):
    if x != 0:
        res += x
        x = int(input())
        summa(x, res)
    else:
        print(res)
        return


a = int(input())
summa(a)
