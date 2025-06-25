def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,s,x = case
        res = min(abs(x[0] - s), abs(x[n-1] - s)) + abs(x[0] - x[n-1])
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    test_cases.append((n,s,x))

results = ourfunc(t,test_cases)
for res in results:
    print(res)