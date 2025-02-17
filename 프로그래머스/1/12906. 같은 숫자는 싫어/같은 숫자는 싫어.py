def solution(arr):
    s = ['start']
    for i in arr:
        if s[-1] == i:
            continue
        s.append(i)
    
    return s[1:]
