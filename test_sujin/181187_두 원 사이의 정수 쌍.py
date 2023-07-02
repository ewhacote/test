from math import sqrt
def solution(r1, r2):
    answer = 0

    for x in range(-r2,r2+1):
        y = sqrt(r2**2 - x**2)
        answer+=int(y)*2+1
    
    for x in range(-r1+1,r1):
        y = sqrt(r1**2 - x**2)
        answer-=int(y)*2+1
        if x**2 + int(y)**2 == r1**2:
            answer+=2
        
    return answer