def ourfunc(t, test_cases):
    results=[]
    for case in test_cases:
        n,p,num,price=case
        # Build and sort the (cost, available shares) pairs
        collection = list(zip(price, num))
        collection.sort(key=lambda x: (x[0], -x[1]))  # sort by cost ascending, then shares descending

        cost = 0
        i = 1  # One resident already notified by Pak Chanek
        it = 0

        if collection[0][0] <= p:
            cost += p  # First share by Pak Chanek

            while i < n and it < len(collection):
                share_cost, available = collection[it]

                forward = min(available, n - i)
                cost += forward * min(share_cost, p)
                i += forward

                it += 1
        else:
            cost = p * n  # All shares from Pak Chanek

        results.append(cost)

    return results

t=int(input())
test_cases=[]
for _ in range(t):
    n,p = map(int, input().split())
    num=list(map(int, input().split())) #the maximum number of residents that each resident can
    price=list(map(int, input().split())) #the cost for each resident to share the announcement
    test_cases.append((n,p,num,price))

results = ourfunc(t,test_cases)
for res in results:
    print(res)