import sys
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7

def solution(S, A, B, C):
    # dp[s][a][b][c] = s개의 곡을 남기고
    # a, b, c 개의 곡을 각 가수가 남겼을 때 앨범 만들 수 있는 경우의 수
    dp = [[[[-1 for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)] for _ in range(S+1)]

    def dfs(s, a, b, c):
        # Base Case: 곡을 모두 다 정했을 때
        if s == 0:
            if a == b == c == 0:
                return 1  # 성공한 경우
            else:
                return 0  # 실패한 경우 (남은 곡 있음)

        # 이미 계산한 경우 → memoization
        if dp[s][a][b][c] != -1:
            return dp[s][a][b][c]

        res = 0

        # 가능한 7가지 조합 → (0,1)의 비트마스크 형태
        for i in range(2):  # dotorya 참여 여부 (0 or 1)
            for j in range(2):  # kesakiyo 참여 여부
                for k in range(2):  # hongjun7 참여 여부
                    if i == j == k == 0:
                        continue  # 최소 한 명은 참여해야 함

                    # 다음 상태 유효한지 확인
                    if a - i >= 0 and b - j >= 0 and c - k >= 0:
                        res = (res + dfs(s - 1, a - i, b - j, c - k)) % MOD

        dp[s][a][b][c] = res
        return res

    return dfs(S, A, B, C)

if __name__ == "__main__":
    S, A, B, C = map(int, sys.stdin.readline().split())
    print(solution(S, A, B, C))
