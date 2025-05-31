import math

def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n, a = case
        overall_gcd = a[0]
        for num in a[1:]:
            overall_gcd = math.gcd(overall_gcd, num)

        gcd_pair=[]
        k=0
        while overall_gcd not in gcd_pair:
            gcd_pair_temp=[]
            for i in range(n):
                for j in range(i+1, n):
                    gcd_pair_temp.append(math.gcd(gcd_pair[i], gcd_pair[j]))
            gcd_pair=gcd_pair_temp
            k+=1
        
        # Check if all elements are already equal to the overall GCD
        if len(set(gcd_pair))==1:
            results.append(0)
            continue
        else:
        # Count the number of elements not equal to the overall GCD
            count = sum(1 for num in a if num != overall_gcd)
            if overall_gcd in gcd_pair:
                results.append(count)
            else:
                results.append(count+k)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n,a))

results = ourfunc(t,test_cases)
for res in results:
    print(res)

#WIP... Currently is faulty