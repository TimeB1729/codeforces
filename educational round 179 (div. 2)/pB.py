def ourfunc(t, test_cases):
    results = []

    # Precompute first 10 Fibonacci numbers (since n ≤ 10)
    fib = [1, 2]
    for _ in range(8):
        fib.append(fib[-1] + fib[-2])

    for case in test_cases:
        n, m, arr = case
        cubes = fib[:n]
        res = []
        for box in arr:
            w,l,h = sorted(box)
            if h >= fib[n-2]+fib[n-1] and w >= fib[n-1]:
                res.append("1")
            else:
                res.append("0")
        results.append(''.join(res))

    return results

# Input Handling
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    test_cases.append((n, m, arr))

results = ourfunc(t, test_cases)
for res in results:
    print(res)
