import sys

"""
연산자(+, -, x) 우선순위 모두 동일
괄호 안에는 하나의 연산자만
중첩된 괄호 X

괄호를 추가해 최댓값 만들기
괄호 개수 제한 없음

# 풀이
- 연산자 마다 괄호 O / X 나눠서 재귀 -> DFS 사용
- 중첩된 괄호 사용하지 못하기 때문에, 인접한 연산자는 앞에 괄호 여부에 따라 영향을 받는다.

# 자료형 선택
- 식의 숫자(nums)와 연산자(operations)을 각각 나눠서 저장
    -> 인덱스 기준 계산이 가능

# 시간 공간 복잡도
- 연산자 최대 개수 9개 -> 재귀로 하면 2^9 = 512

# 구현 설계
1. nums, operations 분리
2.  연산자 위치를 기준으로 dfs
1) 현재 연산자 괄호 X : (cur_value) op (다음 숫자) 처리 -> dfs(index + 1, new_value)
2) 현재 연산자 괄호 O : (cur_value) op1 ((다음 숫자) op2 (다다음 숫자))처리
    -> 다음, 다다음 숫자 계산 temp
    -> cur_value와 temp 연산 : index + 1에 연산자가 있어야 함.
    -> ** cur_value와 op1을 괄호로 묶으면 중첩된 괄호가 계산될 수 있기 때문에 위와 같은 방법 채택
3. 최댓값 갱신
"""

# ----- input -----
input = sys.stdin.readline
L = int(input())
context = input()

# ----- code -----
# initial settings
nums = []
operations = []
INF = sys.maxsize
answer = -INF

for i in range(L):
    if i % 2 == 0:
        nums.append(int(context[i]))
    else:
        operations.append(context[i])


# 연산자 계산 정의
def calc(x, op, y):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    else:
        return x * y


def dfs(index, current_value):
    global answer

    # 마지막 연산자까지 완료했으면 종료
    if index == len(operations):
        answer = max(answer, current_value)
        return

    # 현재 연산자에 괄호 없이 진행
    next_value = calc(current_value, operations[index], nums[index + 1])
    dfs(index + 1, next_value)

    # 현재 연산자에 괄호 넣고 진행
    if index + 1 < len(operations):
        temp = calc(nums[index + 1], operations[index + 1], nums[index + 2])
        new_value = calc(current_value, operations[index], temp)
        dfs(index + 2, new_value)


dfs(0, nums[0])

print(answer)
