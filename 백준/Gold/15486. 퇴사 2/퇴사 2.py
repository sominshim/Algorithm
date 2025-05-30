import sys

def solution(N, time, pay):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i], dp[i - 1])
        end_date = i + time[i - 1] - 1
        if end_date <= N:
            dp[end_date] = max(dp[end_date], dp[i - 1] + pay[i - 1])
    
    return dp[N]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    time, pay = [], []
    for _ in range(N):
        T, P = map(int, sys.stdin.readline().split())
        time.append(T)
        pay.append(P)
    
    print(solution(N, time, pay))    