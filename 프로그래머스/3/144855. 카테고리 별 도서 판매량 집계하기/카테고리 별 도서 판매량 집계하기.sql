SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B
JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC

/*
1. BETWEEN 말고 LIKE '2022-01%'로 하면 성능상 유리한 것은 무엇인가요?
    만약 SALES_DATE에 인덱스가 있다면, 문자열로 변환하는 LIKE 보다
    날짜 자체를 비교하는 BETWEEN이 인덱스를 타기 훨씬 유리합니다. 
    인덱스 친화적 쿼리를 위해서는 BETWEEN이 더 적합하다고 생각합니다.

2. 만약 특정 카테고리의 도서가 1월에 전혀 판매되지 않았다면, 위 쿼리에서 그 카테고리는 어떻게 출력되나요?
    위의 쿼리와 같이 INNER JOIN을 수행하면 기록이 없는 카테고리는 결과에서 누락됩니다.
    만약 판매량이 없는 카테고리의 출력을 원한다면 BOOK 테이블을 기준으로 LEFT JOIN을 수행하고, 
    IFNULL(SUM(SALES), 0) 처리로 0을 출력하도록 합니다.
*/