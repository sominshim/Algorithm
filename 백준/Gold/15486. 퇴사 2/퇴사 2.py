import sys

def max_profit(N, schedules):
    dp = [0] * (N + 2)  # N+1일까지 고려

    for i in range(1, N + 1):
        Ti, Pi = schedules[i - 1]
        # 상담을 선택하지 않는 경우
        dp[i] = max(dp[i], dp[i - 1])
        # 상담을 선택하는 경우
        if i + Ti <= N + 1:
            dp[i + Ti] = max(dp[i + Ti], dp[i] + Pi)

    return max(dp)

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    schedules = [tuple(map(int, input().split())) for _ in range(N)]
    print(max_profit(N, schedules))
