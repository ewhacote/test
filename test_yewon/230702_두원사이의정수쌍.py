# 두원사이의 정수쌍
import math as m

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        max_y=m.floor(m.sqrt(r2**2-x**2))
        min_y=m.ceil(m.sqrt(r1**2-x**2)) if r1>x else 0
        answer+=max_y-min_y+1
    return answer*4