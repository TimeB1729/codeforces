from collections import Counter

def max_segments(A:list) -> int:
    n = len(A)
    suffix_freq = Counter(A)
    
    segments = 0
    curr_set = set()
    
    for i in range(n - 1):
        curr_set.add(A[i])
        suffix_freq[A[i]] -= 1
        if suffix_freq[A[i]] == 0:
            del suffix_freq[A[i]]
        
        if curr_set.issubset(suffix_freq.keys()):
            segments += 1
            curr_set = set()
    
    return segments + 1

def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,a = case
        segments = max_segments(a)
        
        results.append(segments)

    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    test_cases.append((n,a))

results = ourfunc(t,test_cases)
for res in results:
    print(res)