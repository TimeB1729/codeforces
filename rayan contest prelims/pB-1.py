def solve(t, test_cases):
    results = []
    for case in test_cases:
        n, m, k, s = case
        res = 0
        zero_count = 0
        i = 0
        while i < n:
            if s[i] == '0':
                zero_count += 1
            else:
                zero_count = 0

            if zero_count == m:
                res += 1
                zero_count = 0
                i += k
            else:
                i += 1

        results.append(res)
    return results

t = int(input())
test_cases=[]
for _ in range(t):
    n,m,k=map(int,input().split())
    str_s=(input())
    test_cases.append((n,m,k,str_s))

results = solve(t, test_cases)
for res in results:
    print(res)