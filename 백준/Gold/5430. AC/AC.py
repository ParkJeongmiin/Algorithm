import sys

# ----- input -----
input = sys.stdin.readline
T = int(input())

# ----- code -----
for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    arr_str = input().strip()

    if n == 0:
        arr = []
    else:
        arr = arr_str[1:-1].split(",")

    start, end = 0, n
    reverse_flag = False
    error_flag = False

    for cmd in p:
        # 명령어 별 구분
        if cmd == "R":
            reverse_flag = not reverse_flag
        else:
            if start == end:
                error_flag = True
                break

            if not reverse_flag:
                start += 1
            else:
                end -= 1

    if error_flag:
        print("error")
    else:
        answer = arr[start:end]
        if reverse_flag:
            answer.reverse()

        print("[" + ",".join(answer) + "]")
