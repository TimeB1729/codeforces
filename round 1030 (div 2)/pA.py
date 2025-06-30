def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k = case
        res = [0]*n
        if 0<k<n:
            res[0] = 1
            for i in range(k-1):
                res[n-2-i] = 1
        elif k==n:
            res = [1]*n

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k = map(int, input().split())
    test_cases.append((n,k))

results = ourfunc(t,test_cases)
for res in results:
    print("".join(map(str, res)))