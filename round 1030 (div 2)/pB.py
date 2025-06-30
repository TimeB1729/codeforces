t=int(input())
for _ in range(t):
    n = int(input())
    print(2*n - 1)
    for i in range(1,n):
        print(f"{i} {1} {i}")
        print(f"{i} {i+1} {n}")

    print(f"{n} {1} {n}")


