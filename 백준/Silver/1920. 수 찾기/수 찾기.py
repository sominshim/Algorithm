def binary_search(array, target, start, end):
    if start > end:
        return print(0)
    
    mid = (start + end) // 2
    if target == array[mid]:
        return print(1)
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)

n = int(input())
array = list(map(int, input().split()))

m = int(input())
input_arr = list(map(int, input().split()))

array.sort()
for i in range(m):
    binary_search(array, input_arr[i], 0, n-1)
