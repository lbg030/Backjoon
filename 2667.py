from collections import deque
n = int(input())

graph = [ [0] * (n+1) for _ in range(n+1)]
lst = [list(map(str, input())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if lst[i][j] == '1':
            graph[i][j] = 1
# 총 몇단지 인지
cnt = 0

def bfs(x, y):
        answer = deque()
        graph[x][y] = 0
        count = 0
        answer.append([x,y])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while answer:
            # print(answer, count)
            count += 1
            x,y = answer.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    answer.append([nx,ny])
                    
        return count


lstCnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            count = bfs(i,j)
            lstCnt.append(count)
            
print(cnt)
for x in sorted(lstCnt):
    print(x)
