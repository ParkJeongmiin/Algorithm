n = int(input())

def find(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return find(n-1) + find(n-2) + find(n-3)

for _ in range(n):
    num = int(input())
    print(find(num))