import sys
from heapq import heapify, heappop, heappush

def solution(problem_info, commands):
    """
    input: 
        problem_info = 문제 정보 [문제 번호, 난이도] 형태로 저장
        commands = 명령어 모음 recommand/add/solved
    output: print(추천 문제 번호)
    
    """
    problems = {}  # 현재 등록된 문제: {문제번호: 난이도}
    min_heap, max_heap = [], []
    for p, l in problem_info:
        p = int(p)
        l = int(l)
        problems[p] = l
        heappush(min_heap, (l, p))
        heappush(max_heap, (-l, -p))

    # 명령어 처리
    for command in commands:
        if command[0] == "recommend":
            x = int(command[1])
            if x == 1: # 난이도 최대, 문제번호 최대
                while max_heap:
                    l_neg, p_neg = max_heap[0]
                    l = -l_neg
                    p = -p_neg
                    # 현재 problems에 존재하고 난이도가 일치하면 유효
                    if p in problems and problems[p] == l:
                        print(p)
                        break
                    else:
                        heappop(max_heap)
            else: # 난이도 최소, 문제번호 최소
                while min_heap:
                    l, p = min_heap[0]
                    if p in problems and problems[p] == l:
                        print(p)
                        break
                    else:
                        heappop(min_heap)

        elif command[0] == "add":
            p = int(command[1])
            l = int(command[2])
            problems[p] = l
            heappush(min_heap, (l, p))
            heappush(max_heap, (-l, -p))

        elif command[0] == "solved":
            p = int(command[1])
            # 문제 p는 현재 추천 리스트에 반드시 존재하므로, 제거
            if p in problems:
                del problems[p]
        
    return 

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    problem_info = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]    
    m = int(sys.stdin.readline())
    commands = [sys.stdin.readline().split() for _ in range(m)]
    
    solution(problem_info, commands)