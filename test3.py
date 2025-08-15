def Hn(n: int) -> float:
    sum = 1
    if n > 1:
        for m in range(n):
            h = 1/(m+1)
            sum += h
    else:
        sum = 1
    return sum

x=Hn(99)
print(x)