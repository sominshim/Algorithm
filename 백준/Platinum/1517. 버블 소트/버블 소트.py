import sys
input = sys.stdin.readline
result = 0

def merge_sort(start, end):
    global result
    if end-start < 1: return
    m = int(start+(end-start) / 2)
    merge_sort(start, m)
    merge_sort(m+1, end)

    for i in range(start, end+1):
        tmp[i] = A[i]
    
    k = start 
    index1 = start
    index2 = m + 1
    while index1 <= m and index2 <= end:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k #swap 카운트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= end:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

n = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * int(n+1)
merge_sort(1, n)
print(result)