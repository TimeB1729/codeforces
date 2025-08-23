from collections import defaultdict
from random import getrandbits

RB=getrandbits(31)

def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,k,S,T = case
        count=defaultdict(int)
        for x in S:
            s = x%k
            count[min(s, k-s)^RB] += 1

        for y in T:
            t = y%k
            count[min(t, k-t)^RB] -= 1

        res = "YES" if all(v==0 for v in count.values()) else "NO"
        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,k = map(int,input().split())
    arr_S = list(map(int, input().split()))
    arr_T = list(map(int, input().split()))
    test_cases.append((n,k,arr_S,arr_T))

results = ourfunc(t,test_cases)
for res in results:
    print(res)