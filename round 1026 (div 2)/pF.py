def f(x,y):
    return (x%y) + (y%x)

def compute_beauties(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        ans = 0
        mx = a[0]
        output=[]
        for i in range(n):
            ans = max(ans, f(mx, a[i]))
            if a[i] > mx:
                if a[i] >= mx * 2:
                    mx = a[i]
                    for j in range(i):
                        ans = max(ans, f(a[i], a[j]))
                else:
                    mx = a[i]
                    ans = mx
            output.append(str(ans))
        results.append(output)
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n,a))

answers = compute_beauties(test_cases)
for res in answers:
    print(" ".join(map(str, res)))
