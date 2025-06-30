def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

N = 2025
dp = [0] * (N+1)

for i in range(1, N+1):
    if is_prime(i) or i == 1:
        dp[i] = 0
    else:
        found_losing = False
        for d in range(2, i):
            if i % d == 0 and d != i:
                if dp[i - d] == 0:
                    found_losing = True
                    break
        dp[i] = 1 if found_losing else 0

print(sum(dp))
