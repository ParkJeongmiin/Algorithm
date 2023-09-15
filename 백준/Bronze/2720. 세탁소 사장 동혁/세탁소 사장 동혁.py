n = int(input())

for _ in range(n):
    money = int(input())
    for kind in [25, 10, 5, 1]:
        print(money // kind, end = ' ')
        money = money % kind