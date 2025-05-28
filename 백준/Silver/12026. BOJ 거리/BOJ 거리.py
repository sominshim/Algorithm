import sys

def solution(N, street):
    dp = [float('inf')] * N
    dp[0] = 0
    next_block = {'B':'O',
                  'O':'J',
                  'J':'B'}

    for i in range(N-1):
        if dp[i] == float('inf'):
            continue
        for j in range(i+1, N):
            if street[j] == next_block[street[i]]:
                energe = dp[i] + (j-i)**2
                if energe < dp[j]:
                    dp[j] = energe

    return dp[N-1] if dp[N-1] != float('inf') else -1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    street = sys.stdin.readline().strip()

    print(solution(N, street))
