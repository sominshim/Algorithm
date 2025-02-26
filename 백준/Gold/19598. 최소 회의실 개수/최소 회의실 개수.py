import sys
from heapq import heapify, heappop, heappush
def solution(operations):
    room_cnt = 1
    end_que = [0]
    heapify(arr)
    while arr:
        start, end = heappop(arr)
        if end_que[0] <= start: # que의 가장 일찍 끝나는 시간보다 시작시간이 큰 경우
            heappop(end_que)
            heappush(end_que, end)
        else:
            room_cnt += 1
            heappush(end_que, end)
    return room_cnt


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    sol = solution(arr)
    print(sol) 