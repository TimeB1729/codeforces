from functools import lru_cache
from collections import Counter
import time
import sys
sys.setrecursionlimit(20000)


def expected_days_optimized(N, cells):

    # Count cells by number of prisoners
    counter = Counter(cells)
    a_init = counter[1]  # cells with 1 prisoner
    b_init = counter[2]  # cells with 2 prisoners
    c_init = counter[3]  # cells with 3 prisoners
    
    @lru_cache(None)
    def dp(a, b, c):
        if a == 0 and b == 0 and c == 0:
            return 0.0
        
        m = a + b + c  # non-empty cells
        res = N / m  # expected wait until hitting a non-empty cell
        
        if a > 0:
            res += (a / m) * dp(a - 1, b, c)
        if b > 0:
            res += (b / m) * dp(a + 1, b - 1, c)
        if c > 0:
            res += (c / m) * dp(a, b + 1, c - 1)
        
        return res

    return dp(a_init, b_init, c_init)

# The specific case to solve
N=269
prison = [3, 1, 1, 3, 1, 3, 1, 2, 3, 3, 1, 3, 2, 1, 1, 1, 3, 2, 1, 3, 1, 2, 1, 1, 1, 3, 1, 3, 1, 3, 3, 2, 1, 2, 3, 2, 3, 2, 2, 2, 3, 1, 3, 1, 3, 3, 1, 1, 3, 3, 2, 3, 1, 2, 2, 2, 1, 3, 2, 1, 3, 1, 2, 2, 3, 1, 3, 2, 2, 1, 3, 3, 3, 3, 2, 3, 3, 2, 1, 2, 1, 1, 1, 3, 1, 3, 1, 3, 3, 3, 3, 2, 3, 2, 2, 2, 2, 1, 3, 3, 1, 2, 3, 2, 3, 1, 2, 2, 2, 1, 2, 2, 3, 2, 1, 2, 1, 3, 2, 2, 2, 1, 2, 3, 3, 3, 1, 1, 3, 1, 1, 2, 1, 1, 1, 3, 3, 1, 2, 3, 1, 1, 2, 3, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 3, 1, 2, 3, 2, 3, 1, 1, 1, 3, 2, 2, 3, 2, 2, 2, 3, 1, 3, 3, 2, 3, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 3, 2, 2, 3, 2, 1, 1, 2, 3, 1, 2, 1, 1, 1, 2, 3, 2, 1, 2, 3, 3, 2, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 2, 1, 1, 2, 3, 1, 2, 3, 2, 3, 2, 3, 1, 2, 1, 2, 3, 2, 1, 3, 3, 1, 1, 1, 1, 1, 1, 2, 3, 1, 3, 2, 1, 2, 3, 2, 2, 2, 2, 1, 3, 1, 2, 3, 3, 1, 1, 3, 1, 1]

print(f"Solving prison case with {N} cells...")

# Count distribution
counter = Counter(prison)
a = counter[1]  # cells with 1 prisoner
b = counter[2]  # cells with 2 prisoners  
c = counter[3]  # cells with 3 prisoners

print(f"Distribution: {a} cells with 1 prisoner, {b} cells with 2 prisoners, {c} cells with 3 prisoners")
print(f"Total prisoners: {sum(prison)}")
print(f"Total cells: {N}")

# Solve using the optimized method
start_time = time.time()
result = expected_days_optimized(N, prison)
end_time = time.time()

print(f"\nExpected number of days: {result:.10f}")
print(f"Computation time: {end_time - start_time:.4f} seconds")
