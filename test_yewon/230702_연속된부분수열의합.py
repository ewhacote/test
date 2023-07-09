#연속된부분수열의합

def solution(sequence, k):
    n=len(sequence)
    end=0
    sub_sum=0
    answer = []
    for i in range(n):
        while sub_sum<k and end<n:
            sub_sum+=sequence[end]
            end+=1
        if sub_sum==k:
            answer.append([i,end-1,end-1-i])
        sub_sum-=sequence[i]
    answer.sort(key=lambda x:x[2])
    answer=answer[0][:2]
    return answer