def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,m,a = case
        max_a = max(max(a[i]) for i in range(n))
        r_max = [0]*n
        c_max = [0]*m
        count_max = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == max_a:
                    count_max+=1
                    r_max[i]+=1
                    c_max[j]+=1
        
        res = max_a
        for i in range(n):
            for j in range(m):
                if (r_max[i] + c_max[j] - (a[i][j] == max_a)) == count_max:
                    res = max_a - 1
                    break
        
        results.append(res)

    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,m = map(int, input().split()) # n rows, m columns
    a = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        a.append(arr)
    test_cases.append((n,m,a))

results = ourfunc(t,test_cases)
for res in results:
    print(res)