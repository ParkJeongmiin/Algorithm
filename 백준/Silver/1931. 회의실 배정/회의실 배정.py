'''
1. 종료시간 기준으로 오름차순 정렬 후, 시작시간 기준으로 오름차순 정렬해준다.
    b/c [2, 2], [1, 2]로 입력되었을 때,
        시작시간 기준 정렬을 하지 않으면 answer = 1
        시작시간 기준 정렬을 하면 [1, 2], [2, 2]로 answer = 2가 된다.
2. 회의를 진행
    1) 현재 회의의 종료시간 <= 다음 회의의 시작시간:
        다음 회의를 진행
        answer += 1
'''

n = int(input())    # 예정된 회의의 개수

answer = 0
meetings = []

for _ in range(n):
    start, end = map(int, input().split(" "))
    meetings.append((start, end))
    
meetings.sort(key = lambda x : (x[1], x[0]))    # 종료시간 오름차순 정렬 후, 시작시간 오름차순 정렬

time = 0    # 현재 시간
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1
        
print(answer)