def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2

        # mid 시간 내에 몇 명을 처리할 수 있는지 계산
        people = 0
        for time in times:
            people += mid // time
            if people >= n: break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer