import sys
from itertools import combinations

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n # 합배열
C = [0] * m # 합배열 나머지 중복 원소의 개수 저장
result = 0

# 합배열 + %M 연산
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0: # 
        result += 1
    C[remainder] += 1

# 중복수 중 구간(두 원소의 위치)을 찾는 경우의 수를 계산
for i in range(m):
    if C[i] >= 2:
        result += (C[i]*(C[i]-1)) // 2

print(result)