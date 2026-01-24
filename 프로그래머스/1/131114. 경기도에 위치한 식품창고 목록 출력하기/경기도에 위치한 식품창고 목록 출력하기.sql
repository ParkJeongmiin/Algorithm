SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
        COALESCE(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC


/*
1. COALESCE와 IFNULL의 차이점은 무엇인가요?
    IFNULL은 ㅇ니자를 두 개만 받을 수 있는 MySQL 전용함수인 반면, 
    COALESCE는 표준 SQL 함수로 인자를 여러 개 받을 수 있습니다.
    COALESCE(VAL1, VAL2, VAL3, DEFAULT) 처럼 쓰면 NULL이 아닌 첫 번째 값을 반환하므로 훨씬 유리합니다.
    
2. LIKE '%경기도%'와 LIKE '경기도%'의 성능 차이가 있을까요?
    큰 차이가 있습니다. %가 앞에 붙으면 인덱스를 활요하지 못하고, 
    전체 행을 검사(FULL TABLE SCAN)해야 합니다. 주소가 보통 '경기도 ~'로 시작한다면, 
    앞에 %를 뺀 방식을 사용하는 것이 인덱스 활용 측면에서 성능상 훨씬 유리합니다.
    
3. 만약 FREEZER_YN 컬럼에 이미 인덱스가 걸려 있다면, COALESCE를 사용한 필터링에서 주의할 점은?
    WHERE COALESCE(FREEZER_YN, 'N') = 'Y' 처럼
    함수나 연산으로 컬럼을 감싸면 인덱스가 깨지게 됩니다.
    인덱스를 태우려면 컬럼 원본을 유지해야 하기 때문에 다음과 같이 설계해야 합니다.
    WHERE (FREEZER_YN = 'Y')  OR  FREEZER_YN IS NULL
*/