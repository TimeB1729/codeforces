MOD = 998244353
N=1e5+5
s=[]
x=0
s.append(1)
while x < N:
    s.append(2*s[-1] % MOD)
    x+=1


def ourfunc(t, test_cases):
    results = []
    for case in test_cases:
        n, p, q = case
        i=j=k=0
        r=[]
        while k<n:
            if p[k]>p[i]:
                i=k
            if q[k]>q[j]:
                j=k
            if p[i]!=q[j]:
                if p[i]>q[j]:
                    r.append((s[p[i]] + s[q[k-i]]) % MOD)
                else:
                    r.append((s[q[j]] + s[p[k-j]]) % MOD)
            else:
                r.append((s[p[i]] + s[max(q[k-i], p[k-j])]) % MOD)
            k+=1

        results.append(r)
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    test_cases.append((n, p, q))

# Output
results = ourfunc(t, test_cases)
for res in results:
    print(" ".join(map(str, res)))