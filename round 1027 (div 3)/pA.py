def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        s=case
        root=int(s**0.5)
        if root**2==s:
            a=0
            b=root
            results.append((a,b))
        else:
            results.append(-1)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    s=int(input())
    test_cases.append(s)

results = ourfunc(t,test_cases)
for res in results:
    if res==-1:
        print(res)
    else:
        print(' '.join(map(str,res)))