def solve(t, test_cases):
    results=[]
    for i in range(t):
        n,k,h=test_cases[i]
        cur=h[k-1]
        dist=h[k-1]
        sorted_h=sorted(h)
        res=1
        for val in sorted_h:
            if val > cur:
                if val > cur + dist:
                    res=0
                cur = val
                
        results.append("YES" if res==1 else "NO")
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k=map(int, input().split())
    h=list(map(int, input().split()))
    test_cases.append((n,k,h))

res = solve(t,test_cases)
for soln in res:
    print(soln)