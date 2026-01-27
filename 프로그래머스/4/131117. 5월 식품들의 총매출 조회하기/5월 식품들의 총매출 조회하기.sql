SELECT O.PRODUCT_ID, P.PRODUCT_NAME, (O.TOTAL_AMOUNT * P.PRICE) AS TOTAL_SALES
FROM (
    SELECT PRODUCT_ID, SUM(AMOUNT) AS TOTAL_AMOUNT
    FROM FOOD_ORDER
    WHERE PRODUCE_DATE BETWEEN '2022-05-01' AND '2022-05-31'
    GROUP BY PRODUCT_ID
) AS O
JOIN FOOD_PRODUCT P ON O.PRODUCT_ID = P.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC


/*
1. 만약 5월에 주문이 전혀 없는 식품도 '0원'으로 표시해서 목록에 포함해야 한다면 어떻게 수정하시겠습니까?
    현재 쿼리는 INNER JOIN을 수행해 주문량이 없는 물품은 결과에서 제외됩니다.
    FOOD_PRODUCT를 기준으로 LEFT JOIN을 수행하고, COALESCE(TOTAL_SALES, 0) 처리를 진행해야 합니다.
    
2. PRODUCE_DATE 컬럼에 인덱스를 걸 때,
단일 인덱스와 (PRODUCE_DATE, PRODUCT_ID, AMOUNT) 복합 인덱스 중 무엇이 더 유리할까요?
    복합 인덱스가 유리합니다. 테이블 본체에 접근하지 않고, 인덱스만으로 필터링, 그룹화, 합산 연산을 모두 끝낼 수 있습니다.

*/