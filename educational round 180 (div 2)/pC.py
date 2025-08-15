def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,a = case
        ans = 0
        for i in range(n):
            for j in range(i):
                x = max(a[n - 1], 2 * a[i]) - a[i] - a[j]
                left, right = 0, j
                while left < right:
                    mid = (left + right) // 2
                    if a[mid] <= x:
                        left = mid + 1
                    else:
                        right = mid

                k = left
                ans += j - k

        results.append(ans)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n,a))

results = ourfunc(t,test_cases)
for res in results:
    print(res)