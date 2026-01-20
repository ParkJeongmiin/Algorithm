SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP, 
    COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP ASC

/*
1. TRUNCATE 대신 CASE WHEN을 사용해 구간을 나눌 수 있는데, 위 방법을 선택한 이유는?
    CASE WHEN 방식은 가격대가 늘어날 수록 코드를 계속 수정해야하는 문제가 있습니다.
    수식을 사용하게 되면 자동으로 구간을 생성하기 때문에 유지 보수성과 확장성에서 이점이 있습니다.
    
2. PRICE 컬럼에 인덱스가 걸려 있다면, 위 쿼리는 인덱스를 효율적으로 활용(Index Scan)할 수 있을까요?
    함수가 적용된 컬럼의 인덱스 작동원리 확인
    SELECT 절에서 가공하는 것은 문제가 없지만, 만약 WHERE 절에서 수식 조건을 지정하게 되면
    인덱스를 타지 못하고 Full Table Scan이 발생할 수 있습니다.
    조건 절에서는 가공되지 않은 컬럼(PRICE >= 10000 AND PRICE < 20000)을 사용하는 것이 유리하다고 생각합니다.
    
3. 결과 데이터에서 특정 가격대에 상품이 하나도 없다면 어떻게 되나요?
    위의 GROUP BY 쿼리로는 없는 데이터에 대해서는 출력하지 않습니다.
    만약 모든 구간의 값을 보여줘야 한다면 재귀 쿼리나 숫자 테이블을 사용해 뼈대를 먼저 만든 후,
    값을 기입해야 합니다.
*/