import sys
from math import gcd          # **① LCM 계산을 위해**

def solution(M, N, x, y):
    """
    <x:y> 해가 될 때까지 몇 년이 흘러야 하는가?
    """
    answer = 0
    nx, ny = 0, 0              # 현재 해를 M, N 으로 나눈 나머지

    # **② M·N 대신 LCM을 한계로** (그 이상 가면 패턴이 이미 한 바퀴 돌아옴)
    limit = M * N // gcd(M, N)

    # (x, y)가 주기와 같을 때를 위해 0-기반으로 전환
    tx = x % M                 # ex) x==M 이면 0
    ty = y % N                 # ex) y==N 이면 0

    while answer <= limit:
        plus_year = (tx - nx) % M   # **③ 항상 0~M-1 범위를 갖도록 모듈로 연산**
        if plus_year == 0:
            plus_year = M           # 0이면 한 주기(M)만큼 건너뜀

        nx = (nx + plus_year) % M
        ny = (ny + plus_year) % N
        answer += plus_year

        # **④ 0-기반 값끼리 직접 비교** (nx==0 → x로 되돌리는 보정 불필요)
        if nx == tx and ny == ty:
            return answer

    return -1                       # limit을 넘도록 못 찾으면 해가 없음


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        print(solution(M, N, x, y))
