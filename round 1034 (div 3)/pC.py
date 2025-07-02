def ourfunc(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        res = [1] * n

        if n > 2:
            # Precompute prefix_min and suffix_max
            prefix_min = [float('inf')] * n
            suffix_max = [float('-inf')] * n

            for i in range(1, n):
                prefix_min[i] = min(prefix_min[i-1], a[i-1])
            for i in range(n-2, -1, -1):
                suffix_max[i] = max(suffix_max[i+1], a[i+1])

            for i in range(1, n-1):
                if prefix_min[i] < a[i] and suffix_max[i] > a[i]:
                    res[i] = 0
        results.append(res)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = ourfunc(t, test_cases)
for res in results:
    print("".join(map(str, res)))
