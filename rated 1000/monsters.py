def ourfunc(t, test_cases):
    results = []
    for n, k, arr in test_cases:
        a = [x%k if x%k != 0 else k for x in arr]
        ord_ = list(range(n))
        ord_.sort(key = lambda i: a[i], reverse=True)
        res = [i+1 for i in ord_]

        results.append(res)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((n, k, arr))

results = ourfunc(t, test_cases)
for res in results:
    print(" ".join(map(str, res)))
