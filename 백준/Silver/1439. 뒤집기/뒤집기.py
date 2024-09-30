import math

input = input()
cnt = 0
for i in range(len(input) - 1):
    if input[i] != input[i + 1]:
        cnt += 1

print(math.ceil(cnt/2))