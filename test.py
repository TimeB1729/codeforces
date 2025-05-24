t = int(input())
for i in range(t):
    a,b,c=map(int,(input().split()))
    s = (a+b+c)%3
    if s==0:
        x = (a+b+c)//3
        if x>=a and x>=b:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")