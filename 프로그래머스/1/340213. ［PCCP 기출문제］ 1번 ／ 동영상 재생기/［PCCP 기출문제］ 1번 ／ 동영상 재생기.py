def solution(video_len, pos, op_start, op_end, commands):
    def skip(s):
        if op_start <= s <= op_end:
            return op_end
        return s
    
    video_len, pos, op_start, op_end = map(str2sec, [video_len, pos, op_start, op_end])
    
    pos = skip(pos)
    for command in commands:
        if command == "next":
            pos = min(video_len, pos + 10)
        else:
            pos = max(0, pos - 10)
        
        pos = skip(pos)
    
    return sec2str(pos)

def str2sec(time):
    m, s = map(int, time.split(":"))
    return m * 60 + s

def sec2str(sec):
    m, s = divmod(sec, 60)
    return f'{m:02d}:{s:02d}'