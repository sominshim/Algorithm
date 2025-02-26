import heapq
def solution(operations):
    min_heap, max_heap = [], []
    valid = {} # 값의 존재 유무 → True/False
    length = 0 # 힙의 길이

    for operation in operations:
        # 현재 저장된 원소가 없으면 힙 초기화
        if length == 0:
            min_heap, max_heap = [], []

        command, value = operation.split(' ')
        value = int(value)

        if command == "I": # 삽입
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            valid[value] = True
            valid[-value] = True
            length += 1
        elif length > 0: # 삭제
            if value == -1:  # 최솟값 삭제
                removed = heapq.heappop(min_heap)
                valid[removed] = False
                valid[-removed] = False
            else:  # 최댓값 삭제
                removed = heapq.heappop(max_heap)
                valid[removed] = False
                valid[-removed] = False
            length -= 1

    # 힙에서 유효한 값을 찾는 함수 
    def search_valid(heap, valid):
        while heap:
            v = heapq.heappop(heap)
            if valid[v] == True:
                return v
        return 0
    
    max_val = -search_valid(max_heap, valid)
    min_val = search_valid(min_heap, valid)
    
    return [max_val, min_val]