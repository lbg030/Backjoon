from itertools import combinations

n, m = map(int, input().split())

li = [x for x in range(1, n+1)]

li2 = combinations(li, m)

for x in li2:
    print(*x)
