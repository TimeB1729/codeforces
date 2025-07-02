t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    aj = a[j - 1]
    max_val = max(a)
    
    if k > 1:
        print("YES")
    else:  # k = 1
        if aj == max_val:
            print("YES")
        else:
            print("NO")