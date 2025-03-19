# 연속된 A를 찾는다.
# A의 왼쪽, 오른쪽 둘 중 최솟값을 찾는다.

def solution(name):
    # 조이스틱 조작 최소 횟수
    answer = 0

    # 좌/우로 커서 이동 최소 횟수
    min_move = float('inf')
    for i, char in enumerate(name):
        # 1. 상/하 이동
        # A에서 char를 찾는게 빠른지: 오름차순
        # Z에서 char 찾는게 빠른지: 내림차순(Z의 경우, A에서 커서 왼쪽으로 이동: +1)
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 2. 좌/ 우 이동
        # 해당 알파벳 다음부터 연속된 A 찾기

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1  # A 다음
        # 조작 최소 횟수
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
    answer += min_move

    return answer