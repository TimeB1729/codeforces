def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,s = case
        cnt = s.count('1')
        if cnt <= k or n < 2*k:
            res = "Alice"
        else:
            res = "Bob"

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k = map(int, input().split())
    s = input()
    test_cases.append((n,k,s))

results = ourfunc(t,test_cases)
for res in results:
    print(res)