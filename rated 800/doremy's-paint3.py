from collections import Counter
def if_array_good(t,test_cases):
    results=[]
    for case in test_cases:
        n,a=case
        freq = Counter(a)
        if len(set(a))==2:
            x,y=freq.values()
            if n%2 ==0 and x==y:
                results.append("YES")
            elif n%2==1 and abs(x-y)==1:
                results.append("YES")
            else:
                results.append("NO")
        elif len(set(a))==1:
            results.append("YES")
        else:
            results.append("NO")
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    test_cases.append((n,a))

results = if_array_good(t,test_cases)
for res in results:
    print(res)
