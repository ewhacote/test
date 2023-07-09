from collections import deque
def bfs(board,i,j):
    n = len(board)
    m = len(board[0])
    visited=[[999999 for _ in range(m)] for _ in range(n)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque([(i,j)])
    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            while True:
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or nx>=n or ny<0 or ny>=m:
                    break
                
                if board[nx][ny]=="D":
                    queue.append((nx-dx[i],ny-dy[i]))
                    break
                else:
                    visited[nx][ny] = min(visited[nx-dx[i]][ny-dy[i]]+1, visited[nx][ny])
                    if board[nx][ny]=="G":
                        return visited[nx][ny]
                    if nx == n or ny == m:
                        queue.append((nx,ny))
    return -1

def solution(board):
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j]=="R":
                return bfs(board,i,j)
