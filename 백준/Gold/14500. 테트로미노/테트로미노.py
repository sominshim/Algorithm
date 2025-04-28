import sys
sys.setrecursionlimit(10000)  # 혹시 깊게 탐색할 수도 있어서 늘려줌
input = sys.stdin.read
data = input().split()

# 입력 받기
N, M = int(data[0]), int(data[1])
board = []
idx = 2
for _ in range(N):
    board.append(list(map(int, data[idx:idx+M])))
    idx += M

# 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_value = 0  # 최대 합 저장할 변수
visited = [[False]*M for _ in range(N)]  # 방문 체크


def dfs(x, y, depth, total):
    global max_value
    # 4칸을 다 골랐으면
    if depth == 4:
        max_value = max(max_value, total)
        return
    
    # 상하좌우 이동
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, total + board[nx][ny])
            visited[nx][ny] = False  # 다시 되돌리기 (백트래킹)


# 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 모양 따로 체크
def check_extra_shape(x, y):
    global max_value
    center = board[x][y]
    for case in [
        [(0, 1), (0, -1), (1, 0)],  # ㅗ
        [(0, 1), (0, -1), (-1, 0)], # ㅜ
        [(1, 0), (-1, 0), (0, 1)],  # ㅏ
        [(1, 0), (-1, 0), (0, -1)]  # ㅓ
    ]:
        temp_sum = center
        flag = True  # 범위 벗어나는지 체크
        for dx_, dy_ in case:
            nx = x + dx_
            ny = y + dy_
            if 0 <= nx < N and 0 <= ny < M:
                temp_sum += board[nx][ny]
            else:
                flag = False  # 하나라도 범위 초과하면 안 됨
                break
        if flag:
            max_value = max(max_value, temp_sum)



# 전체 보드 돌면서
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])  # 시작점에서 DFS 시작
        visited[i][j] = False
        check_extra_shape(i, j)    # ㅗ모양 체크

print(max_value)
