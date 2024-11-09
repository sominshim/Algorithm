import sys

input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))

# 오름차순 선택정렬
for i in range(n):
    min_value = min(P[i:n])
    min_idx = P[i:n].index(min_value) + i
    # swap
    tmp = P[i]
    P[i] = min_value
    P[min_idx] = tmp

# 각 소요시간의 총합 계산
S = [0] * n
for i in range(n):
    S[i] = S[i-1] + P[i]
print(sum(S))