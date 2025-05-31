def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,a,b=case
        unique_sums=-1
        min_a=min(a)
        max_a=max(a)
        res=-1
        for i in range(n):
            if b[i]!=-1:
                s=a[i]+b[i]
                if unique_sums==-1:
                    unique_sums=s
                else:
                    if unique_sums!=s:
                        res=0
        if res==0:
            res=0
        else:                
            if unique_sums==-1:
                res=(k+min_a)-(max_a)+1
            else:
                if max_a>unique_sums or k+min_a<unique_sums:
                    res=0
                else:
                    res=1
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int, input().split()))
    b=list(map(int,input().split()))
    test_cases.append((n,k,a,b))

results = ourfunc(t,test_cases)
for res in results:
    print(res)