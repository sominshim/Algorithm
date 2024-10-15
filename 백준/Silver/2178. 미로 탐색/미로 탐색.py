from collections import deque

# 미로 탐색 함수
def bfs(maze, n, m):
    # 방향 벡터: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # BFS를 위한 큐 생성
    queue = deque([(0, 0)])  # 시작점 (0, 0)
    # 시작점에서 출발하는 경로의 길이
    maze[0][0] = 1

    while queue:
        x, y = queue.popleft()

        # 도착지점에 도달한 경우 경로의 길이 반환
        if x == n - 1 and y == m - 1:
            return maze[x][y]

        # 현재 위치에서 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 이동할 위치가 미로의 범위를 벗어나지 않고, 이동 가능한 칸(1)인 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # 이동할 칸의 경로 값을 현재 위치의 경로 값 + 1로 갱신
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

# 입력 처리
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 결과 출력
print(bfs(maze, n, m))
