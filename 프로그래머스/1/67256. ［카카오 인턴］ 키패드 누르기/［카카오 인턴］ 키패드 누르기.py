def cal_dist(num1, num2):
    '''
    두 숫자 사이의 거리 계산
    '''
    keypad = {1: (0, 0),
              2: (0, 1),
              3: (0, 2),
              4: (1, 0),
              5: (1, 1),
              6: (1, 2),
              7: (2, 0),
              8: (2, 1),
              9: (2, 2),
              '*': (3, 0),
              0: (3, 1),
              '#': (3, 2)
             }
    x1, y1 = keypad[num1]
    x2, y2 = keypad[num2]

    return abs(x1 - x2) + abs(y1 - y2)


def solution(numbers, hand):
    answer = ''
    locat = {'R':'*',
             'L':'#'}
    for num in numbers:
        # print('--------', num, '--------')
        if num in [1, 4, 7]:
            answer += 'L'
            locat['L'] = num
        elif num in [3, 6, 9]:
            answer += 'R'
            locat['R'] = num
        else:
            dist_l = cal_dist(locat['L'], num)
            dist_r = cal_dist(locat['R'], num)
            if dist_l < dist_r:
                answer += 'L'
                locat['L'] = num
            elif dist_l > dist_r:
                answer += 'R'
                locat['R'] = num
            else:
                if hand == 'left':
                    answer += 'L'
                    locat['L'] = num
                else:
                    answer += 'R'
                    locat['R'] = num
        # print('--------', answer, '--------')

    return answer