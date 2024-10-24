def solve_minesweeper(n, mine_board, player_board):
    # 결과 보드를 초기화
    result_board = [['.'] * n for _ in range(n)]
    mine_exploded = False

    # 8방향 좌표
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    # 각 칸에 대해 처리
    for r in range(n):
        for c in range(n):
            # 플레이어가 연 칸 중에 지뢰가 있는 칸이 있는지 체크
            if player_board[r][c] == 'x' and mine_board[r][c] == '*':
                mine_exploded = True

    # 결과 보드 채우기
    for r in range(n):
        for c in range(n):
            if mine_board[r][c] == '*' and mine_exploded:
                # 지뢰가 터졌으면 모든 지뢰 위치 표시
                result_board[r][c] = '*'
            elif player_board[r][c] == 'x':
                # 지뢰가 아닌 열린 칸에 대해 주변 지뢰 수 계산
                mine_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and mine_board[nr][nc] == '*':
                        mine_count += 1
                result_board[r][c] = str(mine_count)
            elif player_board[r][c] == '.' and not mine_exploded:
                # 열리지 않은 칸은 그대로 둠
                result_board[r][c] = '.'

    # 결과 보드를 문자열 형태로 변환하여 출력
    for row in result_board:
        print(''.join(row))

# 입력 처리
n = int(input())
mine_board = [input().strip() for _ in range(n)]
player_board = [input().strip() for _ in range(n)]

# 함수 호출
solve_minesweeper(n, mine_board, player_board)
