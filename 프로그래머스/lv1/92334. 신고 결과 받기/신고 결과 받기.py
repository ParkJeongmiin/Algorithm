'''
한 유저는 여러 번 신고 가능
"""But 동일한 유저에 대해서는 1 번만 가능 !"""

모든 유저의 신고를 다 더한 뒤,
k 번 이상 신고된 유저는 정지, 정지된 유저를 신고한 모든 유저에게 메일 전송
return = 각 유저별 결과 메일을 받은 횟수

id_list : 전체 이용자
report : "누가 누구를" 신고        *** max(len(report)) = 200,000 ***
k = k 번 이상 신고 당하면 정지
'''
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    id_result = {_:0 for _ in id_list}      # {id : 처리메일 받는 횟수} 최종 결과를 출력하기 위한 dict
    personal_count = defaultdict(list)      # {신고 받은 사람 : [누구한테 신고 받았는지]} 신고 받은 사람이 누구한테 신고 받았는지
    
    for report in report:                   # 보고 내용에 따라
        do, be_did = report.split()
        
        if do not in personal_count[be_did]:    # 신고 받은 사람이 같은 사람한테 신고 당한적이 없으면 추가
            personal_count[be_did].append(do)
    
    for be_did_person in personal_count:
        if len(personal_count[be_did_person]) >= k:     # 신고를 k 번 이상 받은 사람들은
            for name in personal_count[be_did_person]:  # 신고한 사람들에게 메일 보내기
                id_result[name] += 1
                
    answer = list(id_result.values())
    
    return answer