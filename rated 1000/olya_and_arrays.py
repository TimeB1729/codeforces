def solve(t, test_cases):
    results = []
    for case in test_cases:
        n,arr = case
        
        min_values = [min(lst) for lst in arr]
        beauty = min(min_values)

        second_min_values = []

        for i in range(n):
            sorted_list = sorted(arr[i])
            second_min_values.append(sorted_list[1])
        
        sorted_second_min = sorted(second_min_values)
        second_min_sum = sum(sorted_second_min[i] for i in range(1,n))

        beauty += second_min_sum
        
        results.append(beauty)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        mi = int(input())
        a_mi = list(map(int, input().split()))
        arr.append(a_mi)
    test_cases.append((n,arr))

result = solve(t, test_cases)
for res in result:
    print(res)