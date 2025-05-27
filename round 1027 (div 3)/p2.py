from collections import Counter

def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,s=case
        res=can_form_k_good_pairs(n,s,k)
        results.append(res)
    return results

def can_form_k_good_pairs(n: int, s: str, k: int):
    count = Counter(s)
    zeros = count['0']
    ones = count['1']
    half = n // 2

    # We want exactly k good pairs, and (half - k) bad pairs.
    # A good pair needs two same bits: either '00' or '11'
    # A bad pair needs one of each: '01' or '10'
    # So, we need:
    #   - 2*k of same bits (good pairs)
    #   - 2*(half - k) mixed bits (bad pairs)

    for good_zeros in range(0, k + 1):
        good_ones = k - good_zeros

        # Check if we have enough 0s and 1s for good pairs
        if good_zeros * 2 > zeros or good_ones * 2 > ones:
            continue

        rem_zeros = zeros - 2 * good_zeros
        rem_ones = ones - 2 * good_ones

        # Now check if the rest can form (half - k) bad pairs
        if rem_zeros >= (half - k) and rem_ones >= (half - k):
            return "YES"

    return "NO"

t=int(input())
test_cases=[]
for _ in range(t):
    n,k=map(int, input().split())
    s=input()
    test_cases.append((n,k,s))

results = ourfunc(t,test_cases)
for res in results:
    print(res)