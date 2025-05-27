def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,s=case
        k=s.count("1")
        res = k*(k-1)+(n-k)*(k+1)
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n = int(input())
    s = input()
    test_cases.append((n,s))

results = ourfunc(t,test_cases)
for res in results:
    print(res)