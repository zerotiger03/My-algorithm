N, M = map(int, input().split())
A = [_ for _ in map(int, input().split())]
B = []
c = 0
for _ in A:
	if _ < 0:
		c = c + 1
	else:
		B.append(_)
	
if M >= c+1:
	print(sum(B))
else:	
	lst = [[] for _ in range(c+1)]
	i = 0
	for _ in A:
		if _ >= 0:
			lst[i].append(_)
		else:
			i = i + 1
	lst2 = []
	for _ in lst:
		lst2.append(sum(_))
	lst2.sort()
	s = 0
	for _ in range(M):
		s = s + lst2[-1]
		lst2.pop()
	print(s)
	