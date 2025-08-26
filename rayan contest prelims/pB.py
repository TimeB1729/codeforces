# The inefficient string comparison leads to TLE for large n (at 2*10**5)

def solve(t, test_cases):
    results=[]
    for case in test_cases:
        n,m,k,s = case

        quest=("").join('0'*m)
        res=0
        i=0
        while i+m<=n:
            if quest == s[i:i+m]:
                res+=1
                i+=m+k-1
            else:
                i+=1

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