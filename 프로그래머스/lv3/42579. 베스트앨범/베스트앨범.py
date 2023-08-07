def solution(genres, plays):
    answer = []
    
    # genre_play_idx = {장르 : [[해당 노래 재생 횟수 : 해당 노래 고유 번호]]}
    # genre_total_play = {장르 : 전체 재생 횟수}
    genre_play_idx = {}
    genre_total_play = {}
    
    for i in range(len(genres)):
        if genres[i] in genre_play_idx:
            genre_play_idx[genres[i]].append([plays[i], i])
        else:
            genre_play_idx[genres[i]] = [[plays[i], i]]
        if genres[i] in genre_total_play:
            genre_total_play[genres[i]] += plays[i]
        else:
            genre_total_play[genres[i]] = plays[i]
    
    # genre_total_play를 values 값으로 내림차순 정렬
    genre_total_play = sorted(genre_total_play.items(), key = lambda x:x[1], reverse = True)
    
    # for 문으로 genre_total_play의 key 값을 받는다.
    # genre_play_idx[key]를 노래 재생 횟수(내림차순, -x[0]), 노래 고유 번호(오름차순, x[1])으로 정렬
    # genre_play_idx[key][:2, 1]를 answer에 추가
    for genre, _ in genre_total_play:
        genre_play_idx[genre] = sorted(genre_play_idx[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for _, idx in genre_play_idx[genre][:2]]
    
    return answer