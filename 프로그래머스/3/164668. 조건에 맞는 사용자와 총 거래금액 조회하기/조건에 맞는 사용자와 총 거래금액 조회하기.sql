SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER U
JOIN USED_GOODS_BOARD B ON U.USER_ID = B.WRITER_ID
WHERE B.STATUS = 'DONE'
GROUP BY U.USER_ID, U.NICKNAME -- SELECT 절의 비집계 컬럼을 모두 포함
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC

/*
1. WHERE 절에서 70만원 이상 조건을 쓰지 않고, HAVING 절에 쓴 결정적인 이유는 무엇입니까?
    문제에서 사용자의 총 거래 금액의 크기를 기준으로 잡았습니다.
    WHERE 절은 데이터가 그룹화되기 전에 개별 행을 검사하는 단계입니다.
    WHERE 절에서 70만원 이상의 데이터만 필터링 한다면 단일 거래의 금액이 70만원 이상인 데이터만 필터링 될 것입니다.

2. BOARD 테이블이 수억 건이라면, 이 쿼리의 속도를 높이기 위해서 어떤 인덱스를 제안하시겠습니까?
    'STATUS'와 'RITER_ID', 'PRICE'를 묶은 '복합 인덱스'를 제안하겠습니다.
    STATUS = 'DONE'인 데이터를 빠르게 찾고, 
    WRITER_ID로 바로 그룹화하여 PRICE를 합산할 수 있어 '인덱스 스캔'만으로 쿼리를 끝낼 수 있습니다.
    
3. 만약 USER_ID가 같아도 NICKNAME이 도중에 바뀐 이력이 있는 유저라면, 현재 쿼리 결과에 어떤 영향을 줄까요?
    GROUP BY에 NICKNAME까지 포함되어 있기 때문에, 같은 ID에 다른 닉네임은 다른 행으로 집계됩니다.
    이럴 때는 고유값인 USER_ID로만 그룹화를 진행하거나, 
    MAX(NICKNAME) 같은 방식으로 최신 닉네임 하나만 가져오는 등의 설계가 필요합니다.
*/