def solution(seq, k):
    answer = [0, len(sequence) - 1]
    left, right = 0, 0
    sum = seq[0]

    while left>=right && right < len(sequence)
        if sum < k:
            right += 1
            if right < len(seq):
                sum += seq[right]
        elif sum == k
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            sum -= seq[left]
            left +=1
        else:
            sum -= seq[left]
            left += 1
    return answer