def solve(t, test_cases):
    results=[]
    for i in range(t):
        n=test_cases[i]
        res=[-1]*n
        for j in range(n//2):
            res[2*j+1]=3

        if n%2==0:
            res[-1]=2

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    test_cases.append(n)

results=solve(t, test_cases)
for res in results:
    print(' '.join(map(str, res)))