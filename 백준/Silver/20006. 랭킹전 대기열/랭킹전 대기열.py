import sys

def main():
    input = sys.stdin.readline
    P, M = map(int, input().split())  # 플레이어 수, 방 최대 인원 수

    rooms = []  # 각 방: [기준레벨, 플레이어 리스트]

    for _ in range(P):
        level, nickname = input().split()
        level = int(level)

        # 입장 가능한 방 탐색
        entered = False
        for room in rooms:
            room_level, players = room
            if len(players) < M and abs(room_level - level) <= 10:
                players.append((level, nickname))
                entered = True
                break

        # 입장 가능한 방이 없으면 새 방 생성
        if not entered:
            rooms.append([level, [(level, nickname)]])

    # 결과 출력
    for room_level, players in rooms:
        if len(players) == M:
            print("Started!")
        else:
            print("Waiting!")

        # 닉네임 사전순 정렬 후 출력
        for player in sorted(players, key=lambda x: x[1]):
            print(player[0], player[1])

if __name__ == "__main__":
    main()
