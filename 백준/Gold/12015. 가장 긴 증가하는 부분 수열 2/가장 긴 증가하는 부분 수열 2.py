import sys

def binary_search(arr, target):
    """
    Parameters:
        - n (int): 배열 arr의 크기
        - arr (List[int]): 수열
    Returns:
        - 수열의 가장 긴 증가하는 부분 수열의 길이 (int)
    """
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    ascending_arr = [arr[0]]
    for i in range(n):
        if arr[i] > ascending_arr[-1]:
            ascending_arr.append(arr[i])
        else:
            idx = binary_search(ascending_arr, arr[i])
            ascending_arr[idx] = arr[i]
        
    print(len(ascending_arr))