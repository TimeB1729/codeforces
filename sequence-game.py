t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    a = [b[0]]
    for i in range(1, n):
        if b[i] >= b[i-1]:
            a.append(b[i])
        else:
            a.append(1)
            a.append(b[i])
    
    print(len(a))
    print(' '.join(map(str, a)))
