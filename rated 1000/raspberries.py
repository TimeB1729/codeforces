def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,arr=case
        a=[el%k for el in arr]
        if 0 in a:
            res = 0
        else:
            if k in [2,3,5]:
                res=k-max(a)
            else: #k==4
                ct2 = ct3 = 0
                for el in a:
                    if el==2:
                        ct2+=1
                    elif el==3:
                        ct3+=1

                if ct3 >= 1:
                    res = min(1, max(0,2-ct2))
                else:
                    res = max(0, 2-ct2)
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((n,k,arr))

results = ourfunc(t,test_cases)
for res in results:
    print(res)