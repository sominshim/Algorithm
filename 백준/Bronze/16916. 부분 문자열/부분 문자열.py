import sys

def solution(S, P):
    return 1 if P in S else 0


if __name__ == "__main__":
    S = sys.stdin.readline().strip()
    P = sys.stdin.readline().strip()

    print(solution(S, P))