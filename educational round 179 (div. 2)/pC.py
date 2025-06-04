def dict_runs(arr: list) -> dict:
    runs = {}
    if not arr:
        return runs

    current = arr[0]
    count = 1
    max_runs = {current: 1}
    
    for i in range(1, len(arr)):
        if arr[i] == current:
            count += 1
        else:
            max_runs[current] = max(max_runs.get(current, 0), count)
            current = arr[i]
            count = 1
        max_runs[current] = max(max_runs.get(current, 0), count)

    return max_runs

def ourfunc(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        runs = dict_runs(a)
        cost=[]
        for x in runs.keys():
            c = (n-runs[x])*x
            cost.append(c)
        min_cost = min(cost)
        results.append(min_cost)

    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Solve and print results
results = ourfunc(t, test_cases)
for res in results:
    print(res)
