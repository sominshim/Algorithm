from collections import deque
def solution(m, n, puddles):
    """집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return"""
    answer = 0
    q = deque([(0,0)]) # 출발 지점
    d = {'right': (0,1), # 방향
         'down': (1,0)}
    map = []
    for i in range(n+1):
        row = []
        for j in range(m+1):
            if j == 0 or i == 0:
                row.append(0)
            else: 
                row.append(0)
        map.append(row)

    for j, i in puddles:  # 웅덩이
        map[i][j] = -1

    school = (n, m)

    for i in range(1,n+1):
        for j in range(1, m+1):
            if map[i][j] == -1: # puddle
                continue
            if (i,j) == (1,1): # home
                map[i][j] = 1
                continue
            if map[i-1][j] != -1:
                map[i][j] += map[i-1][j]
                if map[i][j-1] != -1:
                    map[i][j] += map[i][j-1]
            elif map[i][j-1] != -1:
                map[i][j] += map[i][j-1]
    
    return map[n][m] % 1000000007

if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2, 2]]

    print(solution(m, n, puddles))  # 출력: 4mb