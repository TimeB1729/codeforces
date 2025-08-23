def solve(t, test_cases):
    results = []
    for i in range(t):
        n, arr_a, arr_b = test_cases[i]
        sum = 1
        arr_diff = [0]*n
        for x in range(n):
            arr_diff[x] = max((arr_a[x]-arr_b[x]), 0)
            sum+= arr_diff[x]
        
        results.append(sum)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    test_cases.append((n, arr_a, arr_b))

res = solve(t, test_cases)
for sol in res:
    print(sol)