def min_operations_to_fashionable(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        a.sort()
        found = False
        min_ops = n

        for i in range(n):
            for j in range(i + 1, n):
                if (a[i] + a[j]) % 2 == 0:
                    ops = i + (n - 1 - j)
                    if ops < min_ops:
                        min_ops = ops
                        found = True

        results.append(min_ops if found else n - 1)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = min_operations_to_fashionable(t, test_cases)
for res in results:
    print(res)
