def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,x,a=case
        l1=[]
        for i in range(n):
            if a[i]==1:
                l1.append(i)
        gap = max(l1)-min(l1)+1
        if gap > x:
            results.append("NO")
        else:
            results.append("YES")
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n,x,a))

results = ourfunc(t,test_cases)
for res in results:
    print(res)