def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        a,x,y = case
        if x > y:
            x, y = y, x
        res = "YES"
        if a in range(x, y):
            res = "NO"

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    a,x,y = map(int, input().split())
    test_cases.append((a,x,y))

results = ourfunc(t,test_cases)
for res in results:
    print(res)