import sys

def solution(n, k, coins):
    dp = [float('inf')] * (k+1)
    dp[0] = 0
    
    for i in coins:
        for j in range(i, k+1):
            dp[j] = min(dp[j], dp[j - i] + 1)

    return dp[k] if dp[k] != float('inf') else -1

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    coins = []
    for _ in range(n):
        coin = int(sys.stdin.readline())
        coins.append(coin)
    
    print(solution(n, k, coins))
