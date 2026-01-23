WITH TOTAL_GRADE AS (
    SELECT EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C' END AS GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT T.EMP_NO, E.EMP_NAME, T.GRADE, 
    CASE
        WHEN T.GRADE = 'S' THEN E.SAL * 0.2
        WHEN T.GRADE = 'A' THEN E.SAL * 0.15
        WHEN T.GRADE = 'B' THEN E.SAL * 0.1
        ELSE 0 END AS BONUS
FROM TOTAL_GRADE T
JOIN HR_EMPLOYEES E ON T.EMP_NO = E.EMP_NO
ORDER BY EMP_NO ASC


/*
1. AVG(SCORE)를 구할 때, 만약 어떤 사원이 한 개 반기의 점수만 있다면 결과가 어떻게 나올까요?
    AVG()는 존재하는 컬럼의 값만 계산합니다. 
    그렇기 때문에 2개 분기 중 하나만 있다 하더라도 평균은 하나의 분기 점수로 계산됩니다.
    꼭 2분기 데이터가 있는 사원들에 대해 계산이 필요하다면, HAVING 절에서 HALF_YEAR 개수가 2개인 데이터만 필터링합니다.
    
2. 성과금 비율(20%, 15% 등)이 매년 바뀐다면 이 쿼리를 매번 수정해야 할까요?
    현재 쿼리에서는 직접 수정을 진행해야 합니다.
    실무에서 매번 수정할 수 없다면, '성과금 비율' 테이블을 따로 운영해 JOIN하여 관리할 수 있습니다.
    
3. HR_GRADE 테이블에 인덱스를 설계한다면 어떤 컬럼 순서가 유리할까요?
    WHERE 절에서는 YEAR를 선행 컬럼으로 두고, 
    GROUP BY와 AVG 연산에 사용되는 EMP_NO와 SCORE를 뒤에 배치한
    (YEAR, EMP_NO, SCORE) 복합 인덱스를 설계해 인덱스 풀 스캔을 유도하겠습니다.
*/