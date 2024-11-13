import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = [int(input()) for i in range(n)]
peny_cnt = 0

while k > 0:
    a = A.pop()
    peny_cnt += k // a
    k = k % a

print(peny_cnt)