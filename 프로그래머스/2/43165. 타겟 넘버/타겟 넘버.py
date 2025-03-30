from collections import deque, defaultdict

def solution(numbers, target):
    """
    input:
        - numbers: 숫자가 담긴 배열
        - target: 타겟 넘버
    return:
        타겟 넘버를 만드는 경우의 수
    """
    q = deque([numbers[0], -numbers[0]])
    tmp = deque()
    n = len(numbers)
    for i in range(1, n):
        while q:
            num = q.popleft()
            tmp.append(num + numbers[i])
            tmp.append(num - numbers[i])
        q, tmp = tmp, q
    
    answer = [1 for i in q if i == target]

    return sum(answer)

if __name__ == "__main__":
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))  