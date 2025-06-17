def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n=case
        L=[1]*n
        if n%2==0:
            for i in range(n//2):
                L[i] = 2*i+1
                L[-i-1] = 2*i + 2
        else:
            for i in range(n//2):
                L[i] = 2*i+1
                L[-i-1] = 2*i + 2
            L[n//2] = n
        results.append(L)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    test_cases.append(n)

results = ourfunc(t,test_cases)
for res in results:
    print(" ".join(map(str,res)))