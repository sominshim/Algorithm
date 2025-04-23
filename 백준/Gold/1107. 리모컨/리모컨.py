import sys

def can_type(num, broken):
    """숫자 버튼만 눌러서 `num`을 입력할 수 있는지 확인"""
    if num == 0:
        return 0 not in broken
    while num:
        if num % 10 in broken:
            return False
        num //= 10
    return True

def solution(target, broken):
    """
    Parameters:
        - n (int): 이동하려는 채널
        - m (int): 고장난 버튼 개수
        - broken (List[int]): 고장난 버튼 번호
    Returns:
        - broken 버튼을 제외한 0~9, +, - 버튼으로, 채널 n으로 이동하기 위해 눌러야 하는 최소 버튼 수 (int)
    """
    # +/- 만 사용하는 경우
    best = abs(n - 100) 

    # 숫자 버튼 입력 후, +/- 이동
    num_buttons = [i for i in range(10) if i not in broken]

    for cand in range(1_000_000):
        if can_type(cand, broken):
            presses = len(str(cand)) + abs(n - cand)
            best = min(best, presses)

    return best

if __name__ == "__main__":
    # 이동하려는 채널 n
    n = int(sys.stdin.readline())
    # 고장난 버튼 개수 m
    m = int(sys.stdin.readline())
    broken = list(map(int, sys.stdin.readline().split()))

    print(solution(n, broken))