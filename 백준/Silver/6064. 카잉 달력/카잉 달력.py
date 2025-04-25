import sys
from math import gcd          # **① LCM 계산을 위해**

def solution(M, N, x, y):
    """
    <x:y> 해가 될 때까지 몇 년이 흘러야 하는가?
    """
    """
    k ≡ x (mod M) and k ≡ y (mod N)를 동시에 만족하는 가장 작은 k, 없으면 -1
    """
    from math import gcd
    lcm = M * N // gcd(M, N)

    k = x                      # k ≡ x (mod M)인 해들만 체크
    while k <= lcm:
        if (k - y) % N == 0:   # 두 번째 조건
            return k
        k += M                 # 다음 해
    return -1



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        print(solution(M, N, x, y))
