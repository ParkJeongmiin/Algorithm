WITH RECURSIVE TIME_TABLE AS (
    SELECT 0 AS HOUR
    
    UNION ALL
    
    SELECT HOUR + 1 FROM TIME_TABLE WHERE HOUR < 23
)

SELECT T.HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM TIME_TABLE T
LEFT JOIN ANIMAL_OUTS A ON T.HOUR = HOUR(A.DATETIME) -- 생성된 시간 테이블을 수정하지 않으면서 조인
GROUP BY T.HOUR
ORDER BY T.HOUR

/*
1. 이 문제에서 COUNT(*)과 COUNT(ANIMAL_ID)의 차이는 어떻게 되나요?
    COUNT(*)은 NULL 포함한 값, COUNT(ANIMAL_ID)는 NULL을 제외한 값이 나옵니다.
    LEFT JOIN 시에는 데이터가 없는 시간대에도 생성된 행이 존재하기 때문에 값이 달라질 수 있습니다.
    
2. 재귀 쿼리 외의 다른 방법은 무엇인가요?
    1) 숫자(0 ~ 23)이 정의된 정적 숫자 테이블을 만들어두고 조인하는 방법이 있을 수 있습니다.
        - 매번 재귀 연산을 할 필요가 없어 대규모 시스템에서 빠르게 동작합니다.
    2) 사용자 정의 변수(SET @HOUR := -1)를 활용할 수 있습니다.
    
3. 만약 시간대 별이 아닌 분 단위로 0 ~ 1439(24시간)까지 집계해야 한다면, 재귀 쿼리의 성능은 어떨까요?
    재귀 쿼리는 반복 횟수가 많아질수록 스택 메모리를 사용하며 성능이 저하될 수 있습니다.
    또한 시스템 설정에 따라 최대 재귀 횟수(max_recursion_depth) 제한에 걸릴 수 있으므로, 
    대량의 시퀀스 생성 시에는 미리 생성된 물리적 수치테이블을 조인하는 것이 더 안전합니다.

*/