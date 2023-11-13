import sys
sys.setrecursionlimit(2000)

def find_emptyroom(chk, rooms):
    if chk not in rooms: # 빈 방이 있으면
        rooms[chk] = chk + 1 # 방 할당하고, 다음 방의 위치 기록
        return chk
    empty = find_emptyroom(rooms[chk], rooms) 
    rooms[chk] = empty + 1
    return empty

def solution(k, room_number):
    answer = []
    assigned_room = {}
    
    for wish_room in room_number:
        empty_room = find_emptyroom(wish_room, assigned_room)
        answer.append(empty_room)
        # print(answer)

    return answer