def lis_length(arr):
    n = len(arr)
    dp = [1] * n  # 모든 원소를 1로 초기화 (각 원소 자체로 길이 1의 수열이 가능)

    # i번째 원소를 마지막으로 하는 LIS의 길이를 계산
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # 증가하는 관계일 때
                dp[i] = max(dp[i], dp[j] + 1)

    # dp 배열에서 가장 큰 값이 LIS의 길이
    return max(dp)

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# LIS 길이 출력
print(lis_length(arr))
