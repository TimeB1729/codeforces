def daytona(t,test_cases):
    results=[]
    for case in test_cases:
        n,arr=case
        x=-sum(arr)
        results.append(x)
    return results    

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    test_cases.append((n,arr))

results=daytona(t,test_cases)
for res in results:
    print(res)