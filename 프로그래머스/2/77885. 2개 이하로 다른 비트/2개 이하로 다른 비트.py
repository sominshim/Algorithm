def binary(num):
    return bin(num)[2:]

def one_continuity(bin_num):
    one_cnt = 0
    for i in range(len(bin_num) - 1, -1, -1):
        if bin_num[i] == '1':
            one_cnt += 1
        else: break
    return one_cnt

def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = binary(num)
        one_cnt = one_continuity(bin_num)
        if one_cnt < 2:
            answer.append(num + 1)
        else:
            answer.append(num + 2**(one_cnt - 1))
    return answer