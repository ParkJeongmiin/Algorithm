def solution(book_time):
    answer = 0
    
    # 고객들의 예약시간 환산
    book_time_min = []
    for start, end in book_time:
        start_min = int(start[:2]) * 60 + int(start[3:])
        end_min = int(end[:2]) * 60 + int(end[3:]) + 10    # 청소시간 10분 포함
        book_time_min.append([start_min, end_min])
    
    book_time_min.sort()

    # 방 배정
    rooms = []
    for reserve in book_time_min:
        if not rooms:
            rooms.append(reserve)
            continue
        
        for idx, room in enumerate(rooms):
            if room[-1] <= reserve[0]:
                rooms[idx] = room + reserve
                break
        else:
            rooms.append(reserve)
    
    return len(rooms)
'''
그리디

손님들의 예약시간을 '분'으로 환산 + 청소시간 10분까지 더해주기
sort() -> 입실시간 빠른 순(작은 순)으로 정렬(오름차순)

1. list가 비어있다면 객실 지정
2. 다음 고객의 입실시간이 있는 방들의 퇴실시간보다 크거나 같으면 그 방에 배정
3. 있는 방들의 퇴실시간을 모두 확인했는데 입실시간 < 퇴실시간이면 새로운 방 배정
'''