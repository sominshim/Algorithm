def solution(citations):
    citations.sort(reverse=True)
    # 본인보다 큰 수의 개수
    arr = [(i+1, c) for i, c in enumerate(citations) if i+1 <= c]
    # print(arr)
    return len(arr)