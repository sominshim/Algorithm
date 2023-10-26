def solution(line):
    point = set()
    # 1. 해를 구한다.
    Xmin, Xmax= int(1e15), int(-1e15)
    Ymin, Ymax= int(1e15), int(-1e15)
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            # 해가 없을 경우 예외처리(평행) > AD - BC = 0
            ad_bc = line[i][0]*line[j][1] - line[i][1]*line[j][0]
            if ad_bc == 0:
                continue
            x = (line[i][1]*line[j][2] - line[i][2]*line[j][1]) / ad_bc
            y = (line[i][2]*line[j][0] - line[i][0]*line[j][2]) / ad_bc

            # 정수 확인 & 최대, 최소 x, y 좌표
            if (x==int(x)) and (y==int(y)):
                point.add((x, y))

                if Xmin > x: Xmin=x
                if Xmax < x: Xmax=x
                if Ymin > y: Ymin=y
                if Ymax < y: Ymax=y

    # 2. 최대, 최소 x, y간의 거리를 구한다 -> 배열을 .으로 초기화한다
    answer = [['.' for _ in range(int(Xmax-Xmin)+1)] for _ in range(int(Ymax-Ymin)+1)]
    # pprint(answer)

    # 3. 최솟값 x를 전체 교점에서 - 빼고, 최댓값 y를 전체 교점에서 -빼고 절댓값을 씌운다.
    # -> 계산된 교점을 *으로 바꾼다.
    for x, y in point:
        answer[int(abs(y-Ymax))][int(x-Xmin)] = '*'

    for i in range(len(answer)):
        answer[i]="".join(answer[i])

    # 4. 배열을 리턴한다.
    return answer
