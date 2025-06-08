def ourfunc(t,test_cases):
    results=[]
    for case in test_cases:
        n,a=case
        a.sort()
        b=[]
        c=[]
        if a[0]==a[-1]:
            results.append(-1)
        else:
            it=0
            while a[it]==a[0]:
                it+=1
            
            lb = it
            lc = n - it
            for i in range(0,it):
                b.append(a[i])
            for j in range(it,n):
                c.append(a[j])
            results.append((lb,lc,b,c))
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    test_cases.append((n,a))

results = ourfunc(t, test_cases)
for res in results:
    if res!= -1:
        lb, lc, b, c = res
        print(lb,lc)
        print(" ".join(map(str,b)))
        print(" ".join(map(str,c)))
    else:
        print(res)