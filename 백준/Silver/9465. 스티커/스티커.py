T = int(input())

for _ in range(T):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(scores[0][0], scores[1][0]))
        continue
    
    scores[0][1] += scores[1][0]
    scores[1][1] += scores[0][0]
    
    for i in range(2, n):
        scores[0][i] += max(scores[1][i-2], scores[1][i-1])
        scores[1][i] += max(scores[0][i-2], scores[0][i-1])
    print(max(scores[0][n-1], scores[1][n-1]))