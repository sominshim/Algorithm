def solution(participant, completion):
    part_dict = {}
    for i in participant: # 참가자 명단 dict 생성
        part_dict[i] = part_dict.get(i, 0) + 1
    for i in completion: # 참가자 명단에서 완주자 명단 제거
        part_dict[i] -= 1
    return dict(map(reversed, part_dict.items()))[1]