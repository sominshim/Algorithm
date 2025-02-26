import heapq
def solution(operations):
    valid = {}
    length = 0
    for operation in operations:
        if length == 0:
            min_heap = []
            max_heap = []
        o, v = operation.split(' ')
        v = int(v)
        if o == "I": # 입력
            heapq.heappush(min_heap, v)
            heapq.heappush(max_heap, -v)
            valid[v] = True
            valid[-v] = True
            length += 1
        elif length > 0:
            if v == -1: # 최솟값 삭제
                removed = heapq.heappop(min_heap)
                valid[removed] = False
                valid[-removed] = False
            else:# 최댓값 삭제
                removed = heapq.heappop(max_heap)
                valid[removed] = False
                valid[-removed] = False
            length -= 1

    def search_vaild(heap, valid):
        while heap:
            v = heapq.heappop(heap)
            if valid[v] == True:
                return v
        return 0
    
    answer = []
    answer.append(-search_vaild(max_heap, valid))
    answer.append(search_vaild(min_heap, valid))
    
    return answer