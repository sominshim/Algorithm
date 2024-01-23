def solution(citations):
    n = len(citations)
    if min(citations) >= n: return n
    
    for h in range(n, 0, -1):
        bigger_cnt = len([e for e in citations if e >= h])
        if bigger_cnt >= h:
            return h
    return 0