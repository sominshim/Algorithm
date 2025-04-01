from collections import deque

def solution(n, computers):
    stack = [0]
    visited = set([0])  # 방문한 좌표 저장
    network_cnt = 1

    while stack:
        curr = stack.pop()

        for i in range(n):
            # 연결 노드(1)이며, 방문하지 않은 경우
            if computers[curr][i] == 1 and i not in visited:
                visited.add(i)
                stack.append(i)
        if not stack:
            # 방문하지 않은 노드 추가
            for i in range(n):
                if i not in visited:
                    stack.append(i)
                    network_cnt += 1
                    break
            
    # 마지막까지 도달하지 못했을 때
    return network_cnt

if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    
    print(solution(n, computers)) # 2 