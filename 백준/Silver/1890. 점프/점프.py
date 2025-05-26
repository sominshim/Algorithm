import sys
from collections import deque

def solution(board, N):
    """
    [0,0] > [N-1, N-1] 까지의 이동 경로 수
    """
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1

    for r in range(N):
        for c in range(N):
            if dp[r][c] == 0 or board[r][c] == 0:
                continue
            move = board[r][c]
            if r + move < N:
                dp[r + move][c] += dp[r][c]
            if c + move < N:
                dp[r][c + move] += dp[r][c]
    
    return dp[N-1][N-1]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution(board, N))