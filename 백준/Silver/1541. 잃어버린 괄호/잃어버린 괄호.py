import sys
input = sys.stdin.readline

str_exp = input()
minus_splited_exp = str_exp.split('-')

result = 0

for i in range(len(minus_splited_exp)):
    plus_splited_exp = minus_splited_exp[i].split('+')
    if i == 0:
        for j in plus_splited_exp:
            result += int(j)
        continue
    for j in plus_splited_exp:
        result -= int(j)

print(result)    