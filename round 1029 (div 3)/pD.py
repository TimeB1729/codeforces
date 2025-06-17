def can_be_written(n,x):
    d=x[1]-x[0]
    for i in range(1,n-1):
        if x[i+1]-x[i] != d:
            return 0
    
    if x[0] - d < 0 or x[-1] + d < 0:
        return 0
    
    if (x[0]-d)%(n+1) == 0:
        return 1
    else:
        return 0

def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,x=case
        res = can_be_written(n,x)
        results.append("YES" if res==1 else "NO")
            
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    x=list(map(int, input().split()))
    test_cases.append((n,x))

results = ourfunc(t,test_cases)
for res in results:
    print(res)