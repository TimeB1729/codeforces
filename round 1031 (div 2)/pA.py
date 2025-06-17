def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        k,a,b,x,y = case
        num = 0
        if x <= y:
            num += max((k-a+x)//x, 0)
            k -= max((k-a+x)//x, 0) * x
            num += max((k-b+y)//y, 0)
        else:
            num += max((k-b+y)//y, 0)
            k -= max((k-b+y)//y, 0) * y
            num += max((k-a+x)//x, 0)

        results.append(num)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    k, a, b, x, y = map(int, input().split())
    test_cases.append((k,a,b,x,y))

results = ourfunc(t,test_cases)
for res in results:
    print(res)