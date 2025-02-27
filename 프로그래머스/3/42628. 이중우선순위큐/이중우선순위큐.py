from heapq import heapify, heappop, heappush

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
            heappush(min_heap, value)
            heappush(max_heap, -value)
            valid[value] = True
            length += 1

        elif length > 0: # 삭제
            if value == -1:  # 최솟값 삭제
                removed = heappop(min_heap)
            else:  # 최댓값 삭제
                removed = -heappop(max_heap)
            if removed in valid:
                del valid[removed]
            length -= 1

    answer = []
    # 힙에서 유효한 값을 찾는 함수 
    while max_heap:
        max_neg = max_heap[0]
        max_value = -max_neg
        # 현재 problems에 존재하고 난이도가 일치하면 유효
        if max_value in valid:
            answer.append(max_value)
            break
        else:
            heappop(max_heap)
    if len(answer) != 1:
        answer.append(0)

    while min_heap:
        min_value = min_heap[0]
        if min_value in valid:
            answer.append(min_value)
            break
        else:
            heappop(min_heap)
    if len(answer) != 2:
        answer.append(0)
    
    return answer
