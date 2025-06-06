import sys
import pprint
def solution(N, arr):
    dp = [[0] * 21 for _ in range(N - 1)] # N행 20열
    dp[0][arr[0]] = 1
    target = arr.pop()
    
    for i in range(N - 2):
        for j in range(21):
            if dp[i][j] == 0:
                continue
            plus_num = j + arr[i + 1]
            minus_num = j - arr[i + 1]
            if plus_num <= 20:
                dp[i + 1][plus_num] += dp[i][j]
            if minus_num >= 0:
                dp[i + 1][minus_num] += dp[i][j]

    # pprint.pprint(dp)
    return dp[N-2][target]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    print(solution(N, arr))