def det_swap(t, test_cases):
    results=[]
    for case in test_cases:
        n, set = case
        if set[0]==1:
            results.append("YES")
        else:
            results.append("NO")
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    set = list(map(int, input().split()))
    test_cases.append((n,set))

results = det_swap(t,test_cases)
for res in results:
    print(res)


    