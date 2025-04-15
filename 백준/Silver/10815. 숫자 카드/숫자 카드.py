N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

n_dict = {}
for num in n_list:
    n_dict[num] = 1

for idx in range(M):
    if m_list[idx] in n_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')