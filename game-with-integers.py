def winner(t, test_cases):
    results=[]
    for n in test_cases:
        if n%3==0:
            results.append("Second")
        else:
            results.append("First")
    return results

t=int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    test_cases.append(n)

results = winner(t, test_cases)
for res in results:
    print(res)
