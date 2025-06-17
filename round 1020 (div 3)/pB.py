def ourfunc(t,test_cases):
    results=[]
    for case in test_cases:
        n,x=case
        res=[]
        if x<n:
            for i in range(x):
                res.append(i)
            for i in range(x+1,n):
                res.append(i)
            res.append(x)
        else:
            res=[i for i in range(n)]
        results.append(res)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, x = map(int, input().split())
    test_cases.append((n,x))

results=ourfunc(t,test_cases)
for res in results:
    print(" ".join(map(str, res)))
