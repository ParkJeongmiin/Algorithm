answer = 0
n = input()
person = input()

# S의 개수 세기, 제거
answer += person.count('S')
person = person.replace('S', '')

# LL가 남아있으면
if len(person) > 0:
    answer += (len(person)//2) + 1
    
print(answer)