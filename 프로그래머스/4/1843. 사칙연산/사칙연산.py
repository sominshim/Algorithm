def solution(arr):
    n = (len(arr) + 1) // 2  # 숫자 개수

    # dp_min[i][j], dp_max[i][j] → i~j 숫자 구간의 최소/최대값
    dp_min = [[float('inf')] * n for _ in range(n)]
    dp_max = [[float('-inf')] * n for _ in range(n)]

    # 숫자 초기화 (길이 1짜리 구간)
    for i in range(n):
        dp_min[i][i] = dp_max[i][i] = int(arr[2 * i])

    # 길이 2 이상 구간 처리
    for length in range(2, n + 1):  # 구간 길이
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):  # k는 연산자 인덱스
                op = arr[2 * k + 1]  # 실제 연산자 위치

                for a in (dp_min[i][k], dp_max[i][k]):
                    for b in (dp_min[k + 1][j], dp_max[k + 1][j]):
                        if op == '+':
                            val = a + b
                        else:  # '-'
                            val = a - b

                        dp_min[i][j] = min(dp_min[i][j], val)
                        dp_max[i][j] = max(dp_max[i][j], val)

    return dp_max[0][n - 1]
