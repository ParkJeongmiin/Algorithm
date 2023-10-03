import sys
sys.setrecursionlimit(2000)

def find(want, rooms):
    if want not in rooms:   # 원하는 방이 비어있는 경우
        rooms[want] = want + 1
        return want
    
    empty = find(rooms[want], rooms)
    rooms[want] = empty + 1
    return empty

def solution(k, room_number):
    
    rooms = dict()
    for num in room_number:
        chk_in = find(num, rooms)
    
    return list(rooms)