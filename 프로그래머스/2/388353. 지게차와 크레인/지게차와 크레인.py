# 크레인 모드
def crane(storage, request):
    """
    일치하는 컨테이너는 꺼내고 주변 확인 후, 외부(0) 또는 내부(1)로 표시
    """    
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == request:
                storage[i][j] = "1"
                update(storage, i, j)                
    

# 지게차 모드
def fork(storage, request):
    """
    일치하는 컨테이너 발견 시, 주변에 하나라도 외부(0)이 존재할 때 변경할 리스트에 저장하고
    변경되는 점을 하나씩 처리하면서 외부와 연결된 점을 업데이트
    -> 실시간으로 바꿔가면 접근이 불가능했던 컨테이너도 꺼내는 문제점이 발생하기 때문
    """
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    changed_idx = []
    
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == request:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if storage[nx][ny] == "0":
                        changed_idx.append((i, j))
                        break
                        
    for i, j in changed_idx:
        storage[i][j] = "0"
        update(storage, i, j)    


# 변경 후 상황 업데이트
def update(storage, x, y):
    """
    주어진 위치 주변에 외부(0)인 지점이 있는지 찾고 하나라도 있다면 입력받은 지점을 외부(0)로 표시
    """
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    flag = False
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if storage[nx][ny] == "0":
            storage[x][y] = "0"
            flag = True
            break
    
    if flag:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if storage[nx][ny] == "1":
                storage[nx][ny] = "0"
                update(storage, nx, ny)


def solution(storage, requests):
    answer = 0
    
    # storage padding
    storage = [list("0" + row + "0") for row in storage]
    storage.insert(0, list("0" * len(storage[0])))
    storage.append(list("0" * len(storage[0])))
    
    for request in requests:
        if len(request) == 1:
            fork(storage, request)
        else:
            crane(storage, request[0])
    
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] not in ["0", "1"]:
                answer += 1
    
    return answer