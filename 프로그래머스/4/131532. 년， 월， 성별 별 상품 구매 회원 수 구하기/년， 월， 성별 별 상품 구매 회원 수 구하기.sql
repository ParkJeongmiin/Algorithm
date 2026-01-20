SELECT YEAR(S.SALES_DATE) AS YEAR, 
    MONTH(S.SALES_DATE) AS MONTH, 
    U.GENDER, 
    COUNT(DISTINCT S.USER_ID) AS USERS -- 1. 구매한 회원 수를 계산하기 때문에 중복을 제거
FROM ONLINE_SALE S
JOIN USER_INFO U ON S.USER_ID = U.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER


/*
1. ONLINE_SALE를 드라이빙 테이블로 둔 이유는 무엇인가요?
    일반적으로 판매 기록이 유저 정보보다 많습니다.
    하지만, 이 문제에서는 성별에 대한 필터링이 필요하므로, 
    옵티마이저는 성별이 있는 회원들만 먼저 걸러내 드라이빙 테이블로 삼을 가능성이 높습니다.

2. 만약 서비스 규모가 커져, ONLINE_SALE 테이블이 수억 건이 된다면, 이 쿼리에서 가장 병목이 생길 지점은?
    'DISTINCT' 연산과 'GROUP BY'가 가장 큰 부하를 줍니다.
    수억 건의 데이터를 메모리에서 정렬하고 중복을 제거하는 것을 매우 무겁기 때문에, 
    월별 / 일별로 집계해둔 통계 테이블을 별도로 운영하거나 파티셔닝을 제안할 수 있습니다.
    
3. YEAR(SALES_DATE) 같은 함수를 WHERE 절에 사용하면 발생할 수 있는 문제는 무엇인가요?
    인덱스가 걸린 컬럼을 함수로 감싸면 인덱스를 타지 못하고 Full Table Scan이 발생합니다.
    범위를 지정하는 방식(WHERE DATE >= '2022-01-01' AND DATE < '2023-01-01')이 훨씬 빠릅니다.
*/