def solution(n, times):
    """
    input:
        - n: 입국심사를 기다리는 사람 수
        - times: 각 심사관이 한 명을 심사하는데 결리는 시간 배열
    output:
        모든 사람이 심사를 받는데 걸리는 시간의 최솟값
    """
    answer = 0
    left, right = 1, min(times) * n
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간까지 심사 가능한 사람 수 계산
        people = 0
        for time in times:
            people += mid // time
            if people >= n: 
                answer = mid
                break

        if people >= n:
            right = mid - 1
        else:
            left = mid + 1

    return answer

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))