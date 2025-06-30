def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,s = case
        res = "No"
        count = {}
        for i in range(n):
            if s[i] in count.keys():
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        if max(count.values()) > 2:
            res = "Yes"
        elif max(count.values()) == 2:
            if s[0] != s[-1]:
                res = "Yes"
            else:
                max_keys = [k for k,v in count.items() if v==2]
                if len(max_keys) > 1:
                    res = "Yes"

        results.append(res)
    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n = int(input())
    s = input()
    test_cases.append((n,s))

results = ourfunc(t,test_cases)
for res in results:
    print(res)