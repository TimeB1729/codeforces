def daytona(t,test_cases):
    results=[]
    for case in test_cases:
        n,k,arr=case
        if k in arr:
            results.append("YES")
        else:
            results.append("NO")
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k=map(int, input().split())
    arr=list(map(int,input().split()))
    test_cases.append((n,k,arr))

results=daytona(t,test_cases)
for res in results:
    print(res)