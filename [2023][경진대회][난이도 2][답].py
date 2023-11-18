N = int(input())
lst = [_ for _ in map(int, input().split())]
lst2 = []
for _ in range(N):
	c = 1
	min = lst[_]
	for i in range(_, N-1):
		if min >= lst[i+1]:
			c = c + 1
			min = lst[i+1]
	lst2.append(c)
lst2[:] = reversed(lst2[:])	
m = lst2.index(max(lst2))
print(abs(N-m), lst2[m])
