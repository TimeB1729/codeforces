N = 5005

# Initialize gcd lookup table
g = [[0]*N for _ in range(N)]
for x in range(N):
    g[x][0] = g[0][x] = g[x][x] = x
for x in range(1,N):
    for y in range(1,x):
        g[x][y] = g[y][x] = g[y][x % y]

def solve(t, test_cases):
    result=[]
    for case in test_cases:
        n, arr = case
        a = [0] + arr
        k = 0
        for i in range(1, n+1):
            k = g[k][a[i]]

        for i in range(1, n+1):
            a[i] //= k

        m = max(a)
        INF = float('inf')
        f = [INF] * (m+2)

        for i in range(1, n+1):
            f[a[i]] = 0
        
        for x in range(m, 0, -1):
            for i in range(1, n+1):
                y = a[i]
                gx_y = g[x][y]
                f[gx_y] = min(f[gx_y], f[x] + 1)

        ans = max(f[1] - 1, 0)
        for i in range(1, n+1):
            if a[i] > 1:
                ans += 1
        
        result.append(ans)
    return result

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

result = solve(t, test_cases)
for res in result:
    print(res)