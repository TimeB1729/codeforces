MOD = 998244353

def ourfunc(t, test_cases):
    results = []
    for case in test_cases:
        n, p, q = case
        
        # Precompute 2^x mod MOD for x in 0..n-1
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        # Convert p and q to a and b where a[j] = 2^p[j], b[j] = 2^q[j]
        a = [pow2[p[i]] for i in range(n)]
        b = [pow2[q[i]] for i in range(n)]
        
        # Initialize r with the first element
        r = [ (a[0] + b[0]) % MOD ]
        
        # Track the best a and b indices so far
        best_a = 0  # index in a[0..i]
        best_b = 0  # index in b[0..i]
        
        for i in range(1, n):
            # Update best_a and best_b for the current i
            if a[i] > a[best_a]:
                best_a = i
            if b[i] > b[best_b]:
                best_b = i
            
            # The maximum sum is either a[best_a] + b[i - best_a] or a[i - best_b] + b[best_b]
            # We need to check both possibilities
            candidate1 = (a[best_a] + b[i - best_a]) % MOD if (i - best_a) >= 0 else 0
            candidate2 = (a[i - best_b] + b[best_b]) % MOD if (i - best_b) >= 0 else 0
            r.append(max(candidate1, candidate2))
        
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

#But this code exceeds time limit for big n (near 1e5)