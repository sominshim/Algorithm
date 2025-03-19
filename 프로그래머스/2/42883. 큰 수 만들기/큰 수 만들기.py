def solution(number, k):
    answer = []  # 문자열 연결을 최적화하기 위해 리스트 사용
    m = len(number) - k  # 숫자 제거 후의 자릿수
    start = 0  # 시작 포인터
    
    while start < len(number):
        end = start + k + 1  # 비교할 윈도우 범위
        if end > len(number):  # 범위를 벗어나지 않도록 조정
            end = len(number)
        
        max_num = '0'
        max_idx = start
        
        # `max()` 대신 직접 최대값 찾기 (시간 복잡도 개선)
        for i in range(start, end):
            if number[i] > max_num:
                max_num = number[i]
                max_idx = i
                if max_num == '9':  # 최댓값을 찾으면 더 이상 탐색 불필요
                    break

        k -= max_idx - start  # 제거된 개수 업데이트
        answer.append(max_num)  # 리스트에 추가 (문자열 결합 최적화)

        start = max_idx + 1  # 최댓값 다음으로 이동

        if k == 0 or len(answer) == m:
            break
    
    # 남아있는 숫자 뒤에 이어붙이기
    answer.extend(number[start:len(number)-k])  
    return ''.join(answer)  # 리스트를 문자열로 변환 (O(N) 최적화)

# 테스트 실행
if __name__ == "__main__":
    number = "9876543210"
    k = 4
    sol = solution(number, k)
    print(sol)  # 98765
