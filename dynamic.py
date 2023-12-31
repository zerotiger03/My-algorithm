# 거스름돈을 주어야 할 때 가장 적은 수로 몇 개를 주어야 할까? (동전은 160원, 100원, 50원, 10원이 있음)

# dynamic의 시간 복잡도

# 최대로 오래 걸리면 ex) 160까지는 그냥 나오고 170은 16번 for문을 돈다 또 sort까지 씀, n이라면 16부터 n-1까지 합이고 이는 n^2에 비례한다 (sort도 마찬가지)
# 즉, n^2에 비례한다.

def dynamic(n):
  lst = [[0, 0], [10, 1], [20, 2], [30, 3], [40, 4], [50, 1], [60, 2], [70, 3], [80, 4], [90, 5], [100, 1], [110, 2], [120, 3], [130, 4], [140, 5], [150, 2], [160, 1]]   # 10원부터 160원까지는 동전의 개수를 지정해준다.
  if (n//10) <= 16:
    return lst[n//10][1]
  # 170원부터는 하나씩 추가해준다
  else:
    for i in range(17, (n//10)+1):
      lst3 = []
      for _ in range(1, i):
        s = (i*10)//lst[_][0]
        k = (i*10) - (s*lst[_][0])
        lst3.append(((lst[lst[_][0]//10][1] * s) + lst[k//10][1]))
      lst3.sort()
      lst.append([i*10, lst3[0]])
    return lst[n//10][1]

dynamic(870)  # return 8
