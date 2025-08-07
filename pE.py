import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    ans = [0] * (n + 1)
    for i in range(n, 0, -1):
        ans[i] = math.lcm(a[i], b[i])

    ch = True
    if ans[1] != a[1]:
        ch = False
    if ans[n] != b[n]:
        ch = False

    for i in range(2, n + 1):
        if math.gcd(a[i - 1], ans[i]) != a[i]:
            ch = False

    for i in range(n - 1, 0, -1):
        if math.gcd(b[i + 1], ans[i]) != b[i]:
            ch = False

    print("YES" if ch else "NO")
