def solve(t, test_cases):
    results=[]
    for case in test_cases:
        n = case
        res=[]
        results.append(res)
    return results

t = int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    test_cases.append((n))

results = solve(t, test_cases)
for res in results:
    print(res)