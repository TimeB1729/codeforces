#B87678

MOD = 10**9 + 7

def solve(t, test_cases):
    results=[]
    for case in test_cases:
        k = case
        b=[1,1,2]
        for _ in range(k-2):
            add=(b[-2]+b[-3])%MOD
            b.append(add)
        
        res=(b[-1]+b[-2])%MOD if k>1 else 2

        results.append(res)
    return results

t = int(input())
test_cases=[]
for _ in range(t):
    k=int(input())
    test_cases.append((k))

results = solve(t, test_cases)
for res in results:
    print(res)