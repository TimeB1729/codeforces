def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,arr=case
        a=[arr[0]]
        for i in range(n):
            if arr[i]-a[-1]<2:
                continue
            else:
                a.append(arr[i])
        res=len(a)
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    test_cases.append((n,arr))

results = ourfunc(t,test_cases)
for res in results:
    print(res)