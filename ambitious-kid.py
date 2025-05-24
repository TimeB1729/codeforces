N=int(input())
arr = list(map(int, input().split()))

itr=abs(arr[0])
for i in range(N):
    if itr>abs(arr[i]):
        itr = abs(arr[i])
    i+=1
print(itr)