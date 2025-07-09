def ourfunc(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        ans = 10**18
        i=0
        while i<n:
            j=i
            while j<n and a[j]==a[i]:
                j+=1
            ans = min(ans, (n+i-j)*a[i])
            i=j
        results.append(ans)

    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = ourfunc(t, test_cases)
for res in results:
    print(res)