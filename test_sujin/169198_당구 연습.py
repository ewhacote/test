def solution(m, n, startX, startY, balls):
    answer = []
    
    for ballX, ballY in balls:
        news = [(-ballX, ballY),(2*m-ballX, ballY),(ballX, -ballY),(ballX, 2*n-ballY)]
        distances = []
        for newX, newY in news:
            if startY==newY:
                if newX<ballX<startX or newX>ballX>startX:
                    continue
            if startX==newX:
                if newY<ballY<startY or newY>ballY>startY:
                    continue
            distances.append((startX - newX)**2+(startY - newY)**2)
        answer.append(min(distances))
    return answer
