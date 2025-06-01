import sys

def solution(n, arr):
    dp = [0] * n
    dp[0] = arr[0]
    max_sum = dp[0]

    for i in range(1, n):
        # 이전 누적합에 지금 원소를 더할지, 새로 시작할지 결정
        dp[i] = max(arr[i], dp[i-1] + arr[i])
        max_sum = max(max_sum, dp[i])

    return max_sum

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution(n, arr))
