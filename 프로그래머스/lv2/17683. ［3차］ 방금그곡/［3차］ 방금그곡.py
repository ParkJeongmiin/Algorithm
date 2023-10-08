def solution(m, musicinfos):
    answer = []
    
    for info in musicinfos:
        start, end, name, paper = map(str, info.split(','))
        played_paper = ''
        
        # 시작, 끝 시간 분으로 환산 + 총 재생 시간 계산
        end_min = int(end[:2]) * 60 + int(end[3:])
        start_min = int(start[:2]) * 60 + int(start[3:])
        play_time = end_min - start_min

        # 기존 악보 변경
        change_table = {'C#' : 'c', 'D#' : 'd', 'F#' : 'f', 'G#' : 'g', 'A#' : 'a'}
        
        for prev, changed in change_table.items():
            if prev in paper:
                paper = paper.replace(prev, changed)
                
            if prev in m:
                m = m.replace(prev, changed)
        
        # 재생된 악보 생성
        for i in range(play_time):
            played_paper += paper[i % len(paper)]
            
        # 악보에 멜로디가 있으면 
        if m in played_paper:
            answer.append([name, play_time, start_min])
            
    answer = sorted(answer, key = lambda x : (-x[1], x[2]))
    
    if answer:
        return answer[0][0]
    else:
        return "(None)"
'''
기억한 멜로디를 재생시간과 제공된 악보를 직접 보면서 비교
1. 음악제목, 재생이 시작되고 끝난 시각, 악보
2. C, C#, D, D#, E, F, F#, G, G#, A, A#, B => 총 12 개
3. 각 음악은 1분에 1개씩
4. 반드시 처음부터 재생되며, 음악길이보다 재생시간이 길면 반복재생된것, 짧을 때는 시작부터 재생시간까지만
5. 일치하는 음악이 여러 개이면, 재생된 시간이 제일 긴 음악 제목을 반환, 시간도 같으면 먼저 입력된 음악제목을 반환
6. 조건에 맞는게 없으면 "(NONE)"

m = 기억한 멜로디 1~1439
musicinfos = [[음악이 시작한 시각, 끝난 시각, 제목, 악보]]  시각(HH:MM)

1. info in musicinfos:
    1) 재생된 시간, 끝난 시간을 minute으로 환산해서, 총 재생시간을 구한다.
    2) for idx in range(재생된 시간):
        idx % 기존악보 ==>  재생된 악보 생성
    
'''