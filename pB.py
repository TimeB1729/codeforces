def solve(t, test_cases):
    results=[]
    for i in range(t):
        n,k,rmp=test_cases[i]
        r0 = []
        count_0=0
        for j in range(n):
            if rmp[j]==0:
                count_0+=1
            else:
                r0.append(count_0)
                count_0=0
        r0.append(count_0)
        res=0
        for x in r0:
            if x>=k:
                res+=1+(x-k)//(k+1)

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k=map(int, input().split())
    rmp=list(map(int,input().split()))
    test_cases.append((n,k,rmp))

res = solve(t,test_cases)
for soln in res:
    print(soln)