import sys

# ----- input -----
input = sys.stdin.readline
N = int(input())


# ----- code -----
def find(node):
    if parents[node] < 0:  # 찾는 노드가 root 노드인 경우
        return node

    parents[node] = find(parents[node])
    return parents[node]


def union(a, b):
    a = find(a)  # root node 번호
    b = find(b)  # root node 번호

    if a == b:  # 이미 같은 그룹인 경우
        return

    if parents[a] > parents[b]:
        a, b = b, a

    parents[a] += parents[b]  # 자식 노드 수 업데이트
    parents[b] = a  # root node 번호 지정


parents = [-1] * N  # 부모 노드 정보
prev_col = dict()  # 이전 열 y 좌표들의 노드 번호
now_col = dict()  # 현재 열 y 좌표들의 노드 번호

prev = int(input())
now_col[prev] = 0  # 제일 처음 노드 저장

for node in range(1, N):  # 1번 노드 부터 순회
    y = int(input())

    if y - prev == 1:  # 정확하게 한 개 차이 나면 노드 병합
        union(node, node - 1)
    elif y <= prev:  # 다음 열로 이동
        prev_col = now_col
        now_col = dict()

    # 이전 열, 같은 행에 노드가 존재하면 노드 병합
    if y in prev_col:
        union(node, prev_col[y])

    # 모든 노드 병합, 열 이동을 마친 후, 현재 노드 정보 업데이트
    now_col[y] = node
    prev = y

answer = 0
for node in parents:
    if node < 0:
        answer += 1

print(answer)
print(N)
