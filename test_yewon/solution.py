#요격시스템
def solution(targets):
    targets.sort(key=lambda x:x[1])
    answer = 0
    end=-1
    for s,e in targets:
        if end <= s:
            answer+=1
            end=e
    return answer