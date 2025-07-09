def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        x=case
        arr=[0,0,0]
        count=0
        while min(arr)<x:
            del(arr[0])
            new_min = arr[0]
            arr.append(2*new_min + 1)
            # Increment the count
            count += 1
            arr.sort()
        
        results.append(count)

    return results

t=int(input())
test_cases=[]
for _ in range(t):
    x = int(input())
    test_cases.append(x)

results = ourfunc(t,test_cases)
for res in results:
    print(res)