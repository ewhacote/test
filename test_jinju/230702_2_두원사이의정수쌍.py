import math
def solution(r1, r2):
    in_cnt = 0
    
    #r2에서 구할 수 있는 포인트 - r1에서 구할 수 있는 포인트
    for x in range(1, r2 + 1):
        y_max = math.floor(math.sqrt(r2**2 - x**2))
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2 - x**2)))
        in_cnt += y_max - y_min + 1
    
    #4분면 위의 점 개수 세는 것이므로 *4
    return in_cnt*4
