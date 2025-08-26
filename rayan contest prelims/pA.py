import math
def solve(t, test_cases):
    results=[]
    for case in test_cases:
        a,b = case
        gcd_ab = math.gcd(a,b)
        res = (a*b)//gcd_ab

        results.append(res)
    return results

t = int(input())
test_cases=[]
for _ in range(t):
    a,b=map(int, input().split())
    test_cases.append((a,b))

results = solve(t, test_cases)
for res in results:
    print(res)