def popcount(x):
    return bin(x).count('1')

def ourfunc(t, test_cases):
    results = []
    for case in test_cases:
        n,k,a = case
        ans = sum(popcount(x) for x in a)

        for j in range(61):
            bb = 1 << j
            for i in range(n):
                if not (a[i] & bb) and k >= bb:
                    ans += 1
                    k -= bb

        results.append(ans)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n,k,a))

results = ourfunc(t, test_cases)
for res in results:
    print(res)
