def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        answer.extend([numbers[i] + e for e in numbers[i + 1:]])
        
    answer = list(set(answer))
    return sorted(answer)