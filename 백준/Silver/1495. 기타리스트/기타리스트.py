import sys
from collections import deque
import pprint

def solution(volumes, songs_len, start, max_volume):
    """
    마지막 곡의 최대볼륨을 구하시오.
    마지막 곡을 연주할 수 없다면 -1
    """
    dp = [[0] * (max_volume + 1) for _ in range(songs_len + 1)]
    dp[0][start] = 1

    for r in range(songs_len):
        for c in range(max_volume + 1):
            if dp[r][c] == 0:
                continue
            if c + volumes[r] <= max_volume:
                dp[r + 1][c + volumes[r]] = 1
            if c - volumes[r] >= 0:
                dp[r + 1][c - volumes[r]] = 1

    # 마지막 곡에서 가능한 볼륨 중 최대값 반환
    for i in range(max_volume, -1, -1):
        if dp[-1][i] != 0:
            return i

    return -1
            

if __name__ == "__main__":
    songs_len, start, max_volume = map(int, sys.stdin.readline().split())
    volumes = list(map(int, sys.stdin.readline().split()))

    print(solution(volumes, songs_len, start, max_volume))