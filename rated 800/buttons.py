def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        a,b,c = case
        c1=c%2
        if a+c1 <= b:
            results.append("Second")
        else:
            results.append("First")
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    a,b,c = map(int, input().split())
    test_cases.append((a,b,c))

results = ourfunc(t,test_cases)
for res in results:
    print(res)