def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        a,b,c,d = case
        n1 = min(a,c)
        n2 = min(b,d)
        if n2 <= n1:
            res = "Gellyfish"
        else:
            res = "Flower" 

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    a,b,c,d = map(int, input().split())
    test_cases.append((a,b,c,d))

results = ourfunc(t,test_cases)
for res in results:
    print(res)