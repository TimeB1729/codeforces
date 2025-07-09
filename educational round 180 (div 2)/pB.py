def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,arr = case
        res = 1
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) <= 1:
                res = 0
        if res == 1:
            if arr == sorted(arr) or arr == sorted(arr, reverse=True):
                res = -1
        
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n,arr))

results = ourfunc(t,test_cases)
for res in results:
    print(res)