def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1])
    
    cut = 0
    for s,e in targets:
        if s>=cut:
            cut=e
            answer+=1
            
    return answer