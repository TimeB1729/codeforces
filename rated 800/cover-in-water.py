def min_actions(t, test_cases):
    results=[]
    for n,s in test_cases:
        i=0
        action_1 = 0
        while i < n:
            if s[i] == '.':
                j = i
                while j < n and s[j] == '.':
                    j += 1
                segment_length = j - i
                if segment_length>2:
                    action_1 = 2
                    break
                else:
                    action_1 += segment_length
                i = j
            else:
                i += 1
        results.append(action_1)
    return results

t=int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n,s))

results = min_actions(t, test_cases)
for res in results:
    print(res)

