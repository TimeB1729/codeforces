t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    s= input()

    counts={}
    for char in s:
        counts[char]=counts.get(char,0)+1

    odd_count=0
    for count in counts.values():
        if count%2 != 0:
            odd_count+=1
    
    if odd_count>k+1:
        print("NO")
    else:
        print("YES")