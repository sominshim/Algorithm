import sys

def solution(name_lens, N, W):
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[N] = 0  # 마지막 이후는 벌점 0

    for i in range(N - 1, -1, -1):
        total_len = 0
        for j in range(i, N):
            total_len += name_lens[j]
            if j > i:
                total_len += 1  # 공백 1칸 추가

            if total_len > W:
                break

            if j == N - 1:
                penalty = 0
            else:
                penalty = (W - total_len) ** 2

            dp[i] = min(dp[i], penalty + dp[j + 1])
    return dp[0]

if __name__ == "__main__":
    N, W = map(int, sys.stdin.readline().split())
    name_lens = [int(sys.stdin.readline())for _ in range(N)]

    print(solution(name_lens, N, W))
