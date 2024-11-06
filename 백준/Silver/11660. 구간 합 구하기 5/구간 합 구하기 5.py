# https://www.acmicpc.net/problem/11660
# 구간 합 5
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 배열 크기, 질의 개수
A = [[0] * (n+1)] # 원본 배열
D = [[0]*(n+1) for _ in range(n+1)] # 합 배열

# A 원본 배열 입력
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# D 합 배열 입력
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

# M개의 질의에 대한 결과값 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(ans)

