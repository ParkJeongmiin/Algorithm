def padovan(n, p):
    """
    파도반 수열 점화식 p(n) = p(n-2) + p(n-2) (n=1, 2, 3 : p(n) = 1)
    """
    if p[n]:
        return p[n]
    else:
        p[n] = padovan(n-2, p) + padovan(n-3, p)
        return p[n]

n = int(input())
targets = []
for _ in range(n):
    targets.append(int(input()))

dp = [0, 1, 1, 1] + [0] * 97

for target in targets:
    print(padovan(target, dp))