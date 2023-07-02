def solution(targets):
    targets.sort(key=lambda x:x[1])
    last_shot = -1
    answer = 0
    
    for target in targets:
        if target[0]>last_shot:
            answer+=1
            last_shot = target[1]-0.5
    return answer 