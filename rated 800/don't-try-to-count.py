def contagion(t,test_cases):
    results=[]
    for case in test_cases:
        n,m,x,s = case
        if n>=m:
            if s in x:
                itr=0
            elif s in x+x:
                itr=1
            else:
                itr=-1
        else:
            found=False
            count=0
            y=x
            while len(y)<4*m:
                if s in y:
                    found=True
                    break
                count+=1
                y+=y
            itr=count if found else -1
        results.append(itr)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,m=map(int, input().split())
    x=input()
    s=input()
    test_cases.append((n,m,x,s))

results=contagion(t,test_cases)
for res in results:
    print(res)