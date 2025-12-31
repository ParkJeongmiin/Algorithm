import sys
from collections import deque

# ----- input -----
input = sys.stdin.readline

N = int(input())
node_info = []
for node_num in range(1, N + 1):
    A, H = map(int, input().split())
    node_info.append((node_num, A, H))

# ----- code -----
# initial setting
INF = sys.maxsize
slots = deque([(-INF, INF, -1, "root")])
tree = [[-1, -1] for _ in range(N + 1)]

# sort by H(asc), A(asc)
node_info.sort(key=lambda x: (x[2], x[1]))

# iterate by node_info
cur_depth = node_info[0][2]
idx = 0

while idx < N:
    next_slots = deque()

    # iterate by depth
    while idx < N and node_info[idx][2] == cur_depth:
        node_num, a, h = node_info[idx]  # calculate node information
        match_flag = False

        # iterate by slots
        while slots:
            min_val, max_val, parent_node, direction = slots[0]

            # when matching in enable
            if min_val < a < max_val:
                slots.popleft()
                match_flag = True

                # parent-child update by direction
                if direction == "L":
                    tree[parent_node][0] = node_num
                elif direction == "R":
                    tree[parent_node][1] = node_num

                # next_slots update
                next_slots.append((min_val, a, node_num, "L"))
                next_slots.append((a, max_val, node_num, "R"))

                break  # check next node
            elif a >= max_val:
                slots.popleft()
                continue
            else:
                print(-1)
                sys.exit()

        # When there is not a single matching area
        if not match_flag:
            print(-1)
            sys.exit()

        idx += 1  # check the node that has cur_depth

    # complete current depth, process next depth nodes
    cur_depth += 1
    slots = next_slots

for i in range(1, N + 1):
    print(*(tree[i]))
