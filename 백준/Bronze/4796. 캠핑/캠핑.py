i = 0
while True:
    l, p, v = map(int, input().split())
    answer = 0
    i += 1
    
    if l+p+v == 0:
        break
        
    answer += (v//p) * l
    
    remain_day = v % p
    if remain_day <= l:
        answer += remain_day
    else:
        answer += l
        
    print("Case %d: %d"%(i, answer))