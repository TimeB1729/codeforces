def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,q,arr = case
        res = 0
        len_k = 0
        for i in range(n):
            if arr[i] <= q:
                len_k += 1
            else:
                if len_k >= k:
                    res += (len_k - k + 1) * (len_k - k + 2) // 2
                len_k = 0
            
        if len_k >= k:
            res += (len_k - k + 1) * (len_k - k + 2) // 2

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k,q = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((n,k,q,arr))

results = ourfunc(t,test_cases)
for res in results:
    print(res)