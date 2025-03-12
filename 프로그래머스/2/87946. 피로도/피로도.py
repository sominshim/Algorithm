from itertools import permutations
def solution(k, dungeons):
    '''return: 유저가 탐험할수 있는 최대 던전 수'''
    # 모든 던전의 경우의 수
    max_clear = 0
    for fatigue in permutations(dungeons, len(dungeons)):
        user_fatigue = k
        clear_dungeons = 0
        for required, consump in fatigue:
            if user_fatigue >= required:
                user_fatigue -= consump
                clear_dungeons += 1
        if clear_dungeons > max_clear:
            max_clear = clear_dungeons
    return max_clear