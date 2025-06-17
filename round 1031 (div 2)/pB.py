def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        w,h,a,b,x1,y1,x2,y2 = case
        if x1==x2:
            if abs(y1-y2) % b == 0:
                results.append("Yes")
            else:
                results.append("No")
        elif y1==y2:
            if abs(x1-x2) % a == 0:
                results.append("Yes")
            else:
                results.append("No")
        
        else:
            if abs(x1-x2) % a == 0 or abs(y1-y2) % b == 0:
                results.append("Yes")
            else:
                results.append("No")
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    w,h,a,b = map(int, input().split())
    x1,y1,x2,y2 = map(int, input().split())
    test_cases.append((w,h,a,b,x1,y1,x2,y2))

results = ourfunc(t,test_cases)
for res in results:
    print(res)