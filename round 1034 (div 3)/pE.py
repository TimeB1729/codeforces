from collections import CO

def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,a = case

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