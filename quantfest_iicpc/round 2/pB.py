#B87678
def solve(t, test_cases):
    results=[]
    for case in test_cases:
        n = case
        E_store=1
        E_current=1
        for i in range(2,n+1):
            E_current = 1 + E_store/i
            E_store+=E_current
        res=int(E_current)
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