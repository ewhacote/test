from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS(start):
    q = deque([start])
    
    while(q):
        y, x, dist = q.popleft()
        
        if board[y][x] == 'G':
            return dist
        
        for i in range(4):
            ny = y
            nx = x
            while(True):
                if 0 <= ny + dy[i] < h and 0 <= nx + dx[i]<w:
                    if board[ny +dy[i]][nx + dx[i]] == 'D':
                        if visited[ny][nx] == False:
                            q.append((ny, nx, dist + 1))
                            visited[ny][nx] = True
                            break
                        else:
                            break
                    else:
                         ny += dy[i]
                         nx += dx[i]
                else:
                    if visited[ny][nx] == False:
                        q.append((ny, nx, dist + 1))
                        visited[ny][nx] = True
                        break
                    else:
                        break
    return -1

def solution(b):
    global board
    global h
    global w
    global visited
    
    board = []
    h = len(b)
    w = len(b[0])
    visited = [[False for i in range(w)] for j in range(h)]
    for i in b : 
        board.append(list(i))
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                visited[i][j] = True
                min_dist = BFS((i,j,0))
                
    return min_dist
                        