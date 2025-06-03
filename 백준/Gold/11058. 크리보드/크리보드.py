import sys

def solution(n):
    dp = [i for i in range(n + 1)]
    for i in range(3, n - 2):
        for j in range(i + 3, n + 1):
            dp[j] = max(dp[j], dp[i] * (j - i - 1), dp[j - 1] + 1)
    
    return dp[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))