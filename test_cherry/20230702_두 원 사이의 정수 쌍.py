import math


def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        hi_r1 = math.sqrt(r2 ** 2 - i ** 2)
        if i > r1:
            hi_r2 = 0
        else:
            hi_r2 = math.sqrt(r1 ** 2 - i ** 2)
        answer += math.floor(hi_r1) - math.ceil(hi_r2) + 1

    return answer*4
