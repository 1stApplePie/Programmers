from collections import deque

def solution(scores):
    answer = 0
    wanho_score = scores[0]
    
    scores.sort(key=lambda x:[-x[0], x[1]])
    queue_scores = deque(scores)
    
    get_in = list()
    min_rank = -1
    
    while queue_scores:
        score = queue_scores.popleft()
        if score == wanho_score:
            if wanho_score[1] >= min_rank:
                min_rank = min(score[1], min_rank)
                get_in.append(sum(score))
                min_rank = score[1]
            else:
                return -1
        if min_rank == -1:
            min_rank = score[1]
            
            get_in.append(sum(score))
            
        elif score[1] >= min_rank:
            min_rank = min(score[1], min_rank)
            get_in.append(sum(score))
            min_rank = score[1]
            
    get_in.sort(reverse=True)
    answer = get_in.index(sum(wanho_score))+1
    
    return answer