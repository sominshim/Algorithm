from collections import deque

def solution(maps):
    q = deque([(0,0)])
    n, m = len(maps), len(maps[0])
    visited = set()
    direction = [[-1, 0], # 위
                 [1, 0], # 아래
                 [0, 1], # 오른쪽
                 [0, -1] # 왼쪽
                 ]
    while q:
        cur_r, cur_c = q.popleft()

        for r, c in direction:
            new_r =  cur_r + r
            new_c = cur_c + c

            if 0 <= new_r < n and \
                0 <= new_c < m and \
                maps[new_r][new_c] == 1 and \
                (new_r, new_c) not in visited:
                
                maps[new_r][new_c] += maps[cur_r][cur_c]
                visited.add((new_r, new_c))
                q.append((new_r, new_c))

    return maps[-1][-1] if (n-1, m-1) in visited else -1

if __name__ == "__main__":
    maps = [[1,0,1,1,1],
            [1,0,1,0,1],
            [1,0,1,1,1],
            [1,1,1,0,1],
            [0,0,0,0,1]]
    
    print(solution(maps))  