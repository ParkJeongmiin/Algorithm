import math

def solution(n, k):
    answer = []
    person = list(range(1, n + 1))
    
    while n != 0:
        method = math.factorial(len(person) - 1)
        idx = (k-1) // method       # 들어갈 숫자의 idx
        k %= method             # k update
        n -= 1                  # 자리수 update
        
        answer.append(person[idx])
        person.remove(person[idx])
    
    return answer