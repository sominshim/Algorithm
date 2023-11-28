def solution(n):
    answer = []
    arr = [[0]*n for i in range(n)]
    num = 1
    x, y = -1, 0
    three = 1
    for i in range(n, 0, -1):
        for j in range(i):
            if three % 3 == 1:
                x = x + 1
            elif three % 3 == 2:
                y = y + 1
            else:
                x, y = x - 1, y - 1
            arr[x][y] = num
            num += 1
        three += 1

    for i in arr:
        [answer.append(e) for e in i if e != 0]
    return answer