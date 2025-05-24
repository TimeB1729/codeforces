def min_tank_capacity(t, test_cases):
    results = []
    for case in test_cases:
        n, x, stations = case
        # Include the start point in the trip
        points = [0] + stations
        # Calculate max distance between consecutive points
        max_gap_points = max((points[i+1] - points[i]) for i in range(n))
        end_gap = 2*(x - points[n])
        max_gap = max(max_gap_points, end_gap)
        results.append(max_gap)
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, x = map(int, input().split())
    stations = list(map(int, input().split()))
    test_cases.append((n, x, stations))

# Output results
results = min_tank_capacity(t, test_cases)
for res in results:
    print(res)
