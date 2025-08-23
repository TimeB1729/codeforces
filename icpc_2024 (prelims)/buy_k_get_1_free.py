def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,C = case
        sorted_C = sorted(C)
        res=[0]*n
        for i in range(1, n+1):
            sum=0
            C_i = sorted_C[:i]
            rev_C_i = C_i[::-1]
            for j in range(i):
                add = rev_C_i[j] if (j+1)%(k+1) != 0 else 0
                sum+=add
            res[i-1] = sum
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k = map(int, input().split())
    arr_C = list(map(int, input().split()))
    test_cases.append((n,k,arr_C))

results = ourfunc(t,test_cases)
for res in results:
    print(' '.join(map(str, res)))