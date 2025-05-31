t = int(input())

for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    obs = [tuple(map(int, input().split())) for _ in range(n)]

    # Initialize possible range of total steps
    l, r = 0, 0
    ranges = [(l, r)]
    possible = True

    # Forward pass to determine valid step range at each point
    for i in range(n):
        if d[i] != -1:
            l += d[i]
            r += d[i]
        else:
            r += 1  # Undetermined step could be 0 or 1

        # Apply the observation constraints
        l = max(l, obs[i][0])
        r = min(r, obs[i][1])

        if l > r:
            possible = False
            break

        ranges.append((l, r))

    if not possible:
        print(-1)
        continue

    # Backtrack to reconstruct the valid sequence of steps
    x = l
    for i in range(n - 1, -1, -1):
        if d[i] != -1:
            x -= d[i]
        else:
            # Choose d[i] = 0 if possible, else d[i] = 1
            if ranges[i][0] <= x <= ranges[i][1]:
                d[i] = 0
            else:
                d[i] = 1
            x -= d[i]

    print(' '.join(map(str,d)))