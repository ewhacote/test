def isWin(board,x,y):
    leftY, rightY = (y-1)%3, (y+1)%3
    if board[x][y] == board[x][leftY] == board[x][rightY]:
        return True
    
    upX, downX = (x-1)%3, (x+1)%3
    if board[x][y] == board[upX][y] == board[downX][y]:
        return True
    
    if (board[x][y]==board[upX][leftY]==board[downX][rightY]) or (board[x][y]==board[upX][rightY]==board[downX][leftY]):
        return True
    
    return False

def solution(board):
    n = len(board)
    
    olst = []
    xlst = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j]=="O":
                olst.append((i,j))
            elif board[i][j]=="X":
                olst.append((i,j))
    
    if len(olst)<len(xlst) or len(olst)>=len(xlst)+2:
        return 0
    
    for x,y in olst:
        if isWin(board,x,y) and len(xlst)!=len(olst)-1:
            return 0

    for x,y in xlst:
        if isWin(board,x,y) and len(xlst)!=len(olst):
            return 0
    
    return 1
