'''
bfs로 탐색하여 길 찾기
배열과 방문확인을 통해 진행
상하좌우에 1 확인후 1 존재시 방문정보 업데이트
'''
import sys
n, m = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().rstrip() for _ in range(n)]#배열
visit = [[0] * m for _ in range(n)]#방문정보
visit[0][0] = 1
queue = [(0,0)]#큐를 통해 이동진행상황 기록, 팝을 통해 이동한 경로기준으로 탐색

while queue:
    x, y = queue.pop(0)
    if x == n-1 and y == m-1:
        #print(visit)
        print(visit[x][y])

    #상하좌우 경로 탐색
    if x+1 < n and matrix[x+1][y] == '1' and visit[x+1][y] == 0:
        visit[x+1][y] = visit[x][y] + 1
        queue.append((x+1, y))
    if y+1 < m and matrix[x][y+1] == '1' and visit[x][y+1] == 0:
        visit[x][y+1] = visit[x][y] + 1
        queue.append((x, y+1))
    if x-1 >= 0 and matrix[x-1][y] == '1' and visit[x-1][y] == 0:
        visit[x-1][y] = visit[x][y] + 1
        queue.append((x-1, y))
    if y-1 >= 0 and matrix[x][y-1] == '1' and visit[x][y-1] == 0:
        visit[x][y-1] = visit[x][y] + 1
        queue.append((x, y-1))
