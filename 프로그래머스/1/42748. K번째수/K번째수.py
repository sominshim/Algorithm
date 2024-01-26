def solution(array, commands):
    answer = []
    
    for c in commands:
        i, j, k = c
        splited_arr = array[i - 1:j]
        splited_arr.sort()
        answer.append(splited_arr[k - 1])
    return answer