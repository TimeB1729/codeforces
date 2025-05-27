t=int(input())
inf=10**9+100

for t_ in range(t):
	n=int(input())
	a=[int(i) for i in input().split()]
	
	tree=[[] for i in range(n)]
	for i in range(n-1):
		p, q=map(int, input().split())
		tree[p-1].append(q-1)
		tree[q-1].append(p-1)
	
	
	dppmx=[None]*n 
	dpnmx=[None]*n 
	#dppmn=[inf]*n
	#dpnmn=[inf]*n
	
	visited=[False]*n
	
	#print(dppmx, dpnmx, a)
	dppmx[0], dpnmx[0]=a[0], -a[0]
	
	qs=0
	queue=[0]
	visited[0]=True
	
	while (qs<len(queue)):
		u=queue[qs]
		qs+=1
		for v in tree[u]:
			if visited[v]==True: continue
			b=a[v]
			dppmx[v]=b+max(0, dpnmx[u])
			dpnmx[v]=-b+max(0, dppmx[u])
			queue.append(v)
			visited[v]=True
			
	print( ' '.join(map(str, dppmx)))
			