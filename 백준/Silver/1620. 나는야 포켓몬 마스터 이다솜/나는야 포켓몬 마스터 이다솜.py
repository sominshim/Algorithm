import sys

n, m = map(int, input().split())
pocketmon = {}
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    pocketmon[name] = i

pocketmon_name = list(pocketmon.keys())
for i in range(m):
    prob = sys.stdin.readline().strip()
    try: # 포켓몬 번호 입력
        num = int(prob)
        print(pocketmon_name[num-1])
    except: # 포켓몬 이름 입력
        print(pocketmon[prob])