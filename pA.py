def solve(t, test_cases):
    results=[]
    for i in range(t):
        x=test_cases[i]
        y=9
        while x>0:
            y=min(y,x%10)
            x//=10
        results.append(y)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    x=int(input())
    test_cases.append(x)

res = solve(t,test_cases)
for soln in res:
    print(soln)