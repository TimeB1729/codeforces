t=int(input())
for _ in range(t):
    a,b=map(int, input().split())
    xk,yk=map(int,input().split())
    xq,yq=map(int,input().split())

    knight_moves= [(a,b),(b,a),(-a,b),(-b,a),(a,-b),(b,-a),(-a,-b),(-b,-a)]

    distinct_pos = set()

    for case in knight_moves:
        dx,dy=case
        x=xk-dx
        y=yk-dy

        if any((x + dx2 == xq and y + dy2 == yq) for dx2, dy2 in knight_moves):
            distinct_pos.add((x,y))
    
    print(len(distinct_pos))