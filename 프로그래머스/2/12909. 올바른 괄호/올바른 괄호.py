# 문자열 s가 올바른 괄호이면 true, 아니면 false return
def solution(s):
    stack = []
    for value in s:
        if (len(stack) != 0) and (value == ")") and (stack[-1] == "("):
            stack.pop()
        else:
            stack.append(value)
            
    if len(stack) != 0:
        return False
               
    return True