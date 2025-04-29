import sys

# DFS로 4칸 탐색
def dfs(x, y, depth, total):
    global max_value
    if depth == 4:
        max_value = max(max_value, total)
        return

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False  # 백트래킹

# 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 모양 따로 처리
def check_t_shape(x, y):
    global max_value
    for shape in t_shapes:
        total = board[x][y]
        valid = True
        for dx_, dy_ in shape:
            nx, ny = x + dx_, y + dy_
            if 0 <= nx < N and 0 <= ny < M:
                total += board[nx][ny]
            else:
                valid = False
                break
        if valid:
            max_value = max(max_value, total)

if __name__ == "__main__":
    global N, M, board, visited, dx, dy, t_shapes, max_value
    sys.setrecursionlimit(10000)

    input = sys.stdin.read
    data = list(map(int, input().split()))

    N, M = data[0], data[1]
    board = [data[i*M+2:(i+1)*M+2] for i in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 형태
    t_shapes = [
        [(-1, 0), (0, -1), (0, 1)],  # ㅗ
        [(1, 0), (0, -1), (0, 1)],   # ㅜ
        [(0, -1), (-1, 0), (1, 0)],  # ㅓ
        [(0, 1), (-1, 0), (1, 0)]    # ㅏ
    ]

    max_value = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j])
            visited[i][j] = False
            check_t_shape(i, j)

    print(max_value)