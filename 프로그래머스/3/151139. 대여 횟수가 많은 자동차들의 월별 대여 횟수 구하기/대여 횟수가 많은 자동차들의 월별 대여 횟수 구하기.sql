WITH RENTAL_COUNTS AS (
    SELECT *, 
            COUNT(*) OVER (PARTITION BY CAR_ID) AS TOTAL_RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
)
SELECT MONTH(START_DATE) AS MONTH, 
        CAR_ID, 
        COUNT(*) AS RECORDS
FROM RENTAL_COUNTS
WHERE TOTAL_RECORDS >= 5
GROUP BY MONTH, CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC

/*
1. WHERE 절에서 기간을 2번(서브쿼리와 메인쿼리) 쓰는 이유는?
    서브쿼리에서 기간은 총 기간 중 대여 횟수를 구하기 위해 필터링 했고, 
    메인쿼리에서 기간은 추출된 ID중에서 기간 조건에 만족하는 결과만 필터링하기 위해 사용했습니다.
    메인쿼리의 기간 조건이 없으면 총 기간에 대한 결과를 출력합니다.
    
2. DATE_FORMAT 대신 BETWEEN을 사용한 이유는 무엇인가요?
    인덱스 활용의 경우 성능 차이가 발생할 수 있습니다.
    DATE_FORMAT처럼 컬럼을 함수로 감싸게 되면 인덱스를 타지 못하고 테이블 전체 탐색을 할 확률이 높습니다.
    컬럼 원본을 유지하므로 인덱스를 효율적으로 사용해 수백만 건의 데이터에서도 빠르게 범위를 찾을 수 있습니다.
    
3. HAVING COUNT(*) >= 5를 서브쿼리에서 사용한 이유는 무엇인가요?
    기간 내에 총 대여 횟수가 5회 이상이라도 월별로 쪼갠 후에는 대여 횟수가 5회 미만일 수 있습니다.
    메인 쿼리에서 해당 조건을 설정하게되면 위와 같은 결과를 잡을 수 없습니다.
*/