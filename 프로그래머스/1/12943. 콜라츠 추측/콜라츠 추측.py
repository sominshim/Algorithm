def solution(num, answer=0):
    if num == 1:
        return answer
    elif answer >= 500: # 반복횟수 조건
        return -1
    elif num % 2 == 0: # 짝수
        return solution(num / 2, answer + 1)
    else: # 홀수
        return solution(num * 3 + 1, answer + 1)
