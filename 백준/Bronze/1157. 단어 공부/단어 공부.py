from collections import Counter
input = input()

input = input.lower() # 소문자 변경
cnt = Counter(input)
most_cnt = cnt.most_common(1)[0][1]
c = Counter(cnt.values())

if c[most_cnt] == 1:
    print(cnt.most_common(1)[0][0].upper())
else:
    print('?')