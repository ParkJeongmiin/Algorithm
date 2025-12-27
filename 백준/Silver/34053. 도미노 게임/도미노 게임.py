import sys

"""
N X M 격자 -> a_ij 정수
그래프 탐색, a_ij 반복
=> O(A N^2) 10^15

# 0인 칸이 하나라도 존재
-> 해당 칸을 무조건 포함시키면서 0인 칸을 확장
=> 최대 차례 수 = 모든 칸 수의 합

# 0인 칸이 없다면
-> 최소 값의 칸을 0으로 만들어서 위에 처럼 0인 칸을 확장
=> 최대 차례 수 = (모든 칸 수의 합) - (최소 값)

==> 결과는 (모든 칸 수의 합) - (최소 값)
"""
# ----- input -----
input = sys.stdin.readline

N, M = map(int, input().split())

# ----- code -----
answer = 0
min_val = 10**10

for _ in range(N):
    num_list = list(map(int, input().split()))

    min_val = min(min_val, min(num_list))
    answer += sum(num_list)

print(answer - min_val)
