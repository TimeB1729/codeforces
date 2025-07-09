def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,q,arr = case
        
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k,q = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((n,k,q,arr))

results = ourfunc(t,test_cases)
for res in results:
    print(res)