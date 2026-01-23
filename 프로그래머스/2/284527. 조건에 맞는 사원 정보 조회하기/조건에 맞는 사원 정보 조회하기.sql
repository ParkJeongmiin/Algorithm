WITH TOTAL_SCORE AS (
    SELECT EMP_NO, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT SCORE, EMP_NO, EMP_NAME, POSITION, EMAIL
FROM (
    SELECT T.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL, 
        RANK() OVER (ORDER BY T.SCORE DESC) AS RNK
    FROM TOTAL_SCORE T
    JOIN HR_EMPLOYEES E ON T.EMP_NO = E.EMP_NO
) AS RESULT
WHERE RNK = 1 -- 공동 1등을 모두 출력하기 위한 설계
ORDER BY SCORE DESC

/*
WITH 절을 사용해 '무엇을 집계'하고, 메인 쿼리에서 '어떻게 보여주는지' 높은 가독성
윈도우 함수를 사용해 LIMIT에 비해 원하는 출력에 대해 높은 확장성을 가지고 있습니다.
HR_GRADE에서 필터링, 그룹화를 진행해 데이터 행의 수를 줄이고, JOIN을 수행해 효율적입니다.

1. 만약 한 사원이 연도별로 소속 부서가 바뀌었다면,
    현재 쿼리에서 부서별 1등을 뽑을 때 어떤 문제가 생길 수 있고, 이를 어떻게 해결하시겠습니까?
    
    현재 쿼리는 HR_EMPLOYEES에 현재 시점의 부서 정보를 가져옵니다.
    과거 시점 부서 이력을 적용해야 한다면, 인사 발령 당시 이력 테이블을 추가로 JOIN 하거나, 
    평가 당시 부서 코드가 담긴 테이블을 기준으로 PARTITOIN BY 를 적용해야 합니다.
*/