N, B = map(int, input().split())
S = 0
for _ in range(N):
	s, T = map(int, input().split())
	if T == 1:
		S = S - B
	else:
		S = S + s
print(S)
