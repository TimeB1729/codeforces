def compute_beauties(test_cases):
    results = []

    for a in test_cases:
        n = len(a)
        max1 = a[0]
        max2 = -1
        beauties = [0]  # beauty for prefix of length 1 is 0 (only one element)

        current_max_beauty = 0
        for i in range(1, n):
            x = a[i]
            candidates = []
            if max1 != x:
                candidates.append((x % max1) + (max1 % x))
            if max2 != -1 and max2 != x:
                candidates.append((x % max2) + (max2 % x))
                current_max_beauty = max([current_max_beauty] + candidates)
            beauties.append(current_max_beauty)

            # Update max1 and max2
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x

        results.append(beauties)

    return results

# Read input and run the function
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append(a)

answers = compute_beauties(test_cases)

# Output results
for res in answers:
    print(" ".join(map(str, res)))
