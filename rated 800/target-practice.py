def score(t,test_cases):
    results=[]
    for case in test_cases:
        score=0
        arr=case
        for i in range(10):
            for j in range(10):
                if arr[i][j]=="X":
                    ring = min(i,j,9-i,9-j)
                    score+=ring+1
        results.append(score)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    arr=[input().strip() for _ in range(10)]
    test_cases.append(arr)

results=score(t,test_cases)
for res in results:
    print(res)