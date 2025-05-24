def drop_last_closing_bracket(s):
    idx = s.rfind(')')
    if idx == -1:
        return s  # No ')' found
    return s[:idx] + s[idx+1:]

def can_be_unbalanced(t, test_cases):
    results = []
    for s in test_cases:
        count_opens = 0
        unbalanced_possible = False
        new_s=drop_last_closing_bracket(s)
        for ch in new_s:
            if ch == '(':
                count_opens+=1
            else:  # ch == ')'
                count_opens-=1

            if count_opens==0:
                unbalanced_possible=True
                break
        results.append("YES" if unbalanced_possible else "NO")
    return results

t = int(input())
test_cases = []
for _ in range(t):
    s=input().strip()
    test_cases.append(s)

results = can_be_unbalanced(t, test_cases)
for res in results:
    print(res)
