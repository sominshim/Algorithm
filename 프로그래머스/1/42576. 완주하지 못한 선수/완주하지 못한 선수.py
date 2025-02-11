def solution(participant, completion):
    part_dict = {}
    for name in participant: # 참가자 명단 dict 생성
        part_dict[name] = part_dict.get(name, 0) + 1
    for name in completion: # 참가자 명단에서 완주자 명단 제거
        part_dict[name] -= 1
    return dict(map(reversed, part_dict.items()))[1]