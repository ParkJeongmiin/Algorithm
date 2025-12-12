def alpha_to_num(word):
    value = 0
    for idx, char in enumerate(word[::-1]):
        value += (ord(char) - ord('a') + 1) * (26 ** idx)
    return value


def num_to_alpha(num):
    alpha = ''
    while num > 0:
        mod = (num - 1) % 26
        alpha = chr(mod + 97) + alpha
        num = (num - 1) // 26
    return alpha
    

def solution(n, bans):    
    # bans을 10진수로 변경
    num_bans = []
    for ban in bans:
        num_bans.append(alpha_to_num(ban))
    num_bans.sort()
    
    # 최종 target number 계산
    for idx in range(len(num_bans)):
        if n >= num_bans[idx]:
            n += 1
        else:
            break
    
    return num_to_alpha(n)