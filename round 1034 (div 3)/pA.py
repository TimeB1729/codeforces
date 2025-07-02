def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n = case
        if n%4==0:
            res = "Bob"
        else:
            res = "Alice"
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n = int(input())
    test_cases.append(n)

results = ourfunc(t,test_cases)
for res in results:
    print(res)