import sys
import itertools
def solution(n, k):
    """
    Parameters:
        - n (int): 2차원 배열 A의 크기
        - k (int): 찾고 싶은 일차원 배열 B의 위치
    Returns:
        - B를 오름차순 정렬했을 때, B[k]를 구해보자. (int)
    """
    def count_less_equal(x):
        # A[i][j] <= x인 값의 개수를 세는 함수
        count = 0
        for i in range(1, n+1):
            count += min(x // i, n)
        return count
    
    left, right = 1, n*n

    while left <= right:
        mid = (left + right) // 2

        less_cnt = count_less_equal(mid)
        
        if less_cnt < k:
            left = mid + 1
        else: 
            answer = mid
            right = mid - 1
    return answer

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    print(solution(n, k))